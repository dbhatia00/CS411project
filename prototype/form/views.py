from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from form.models import User, Song
#from .forms import NameForm
import requests
import json
import spotipy
import pandas as pd
import re
import os
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# Create your views here.

def login(request):
	# do upon logout #
	User.objects.all().delete()
	Song.objects.all().delete()
	# end do upon logout #
	return render(request, 'login.html', {})

def form(request):
	# do upon login #
	user = request.user
	spot_login = user.social_auth.get(provider='spotify')
	url = "https://api.spotify.com/v1/me"
	headers={'Accept':'application/json', 'Authorization':"Bearer "+ spot_login.extra_data['access_token']}
	#print(spot_login.extra_data['access_token'])
	r = requests.get(url, headers=headers).content
	data = json.loads(r.decode('utf-8'))
	disp_name = data['display_name']
	user_id = data['id']
	#print(user_id)
	#print(disp_name)
	User.objects.create(name=disp_name, user_id=user_id)
	# replace 2 below with real song lookups
	Song.objects.create(title='Great Song Title', artist='GOAT Artist')
	Song.objects.create(title='Awful Song Title', artist='Terrible Artist')
	# end do upon login #

	users = User.objects.all()
	songs = Song.objects.all()
	context = {
		'users' : users,
		'songs' : songs
	}
	return render(request, 'form.html', context)

def song_title(request):
	#PULL ARTIST NAME FROM SONG TITLE
	user = request.user
	spot_login = user.social_auth.get(provider='spotify')
	data = request.GET['song-title']
	url = 'https://api.spotify.com/v1/search?q='+data+'&type=track&market=US&limit=1'
	headers={'Accept':'application/json', 'Authorization':"Bearer "+ spot_login.extra_data['access_token']}
	r = requests.get(url, headers=headers).content
	r = json.loads(r.decode('utf-8'))['tracks']['items'][0]['album']['artists'][0]['name']

	#USE GET_LYRICS FUNCTION TO PULL LYRICS
	r = get_lyrics(r, data)
	
	# tone analyzer object 
	analyzer = toneAnalyzer()

	# do tone analysis
	result = analyzer.analyze_tone(r)

	return render(request, 'song-title.html', {'data':result})

def get_lyrics(artist, song):
    artistname = str(artist.replace(' ','-')) if ' ' in artist else str(artist)
    songname = str(song.replace(' ','-')) if ' ' in song else str(song)
    url = 'https://genius.com/'+ artistname + '-' + songname + '-' + 'lyrics'
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    cs = soup.select('div[class^="Lyrics__Container"]')
    if cs:
        elements = cs
    else:
        elements = soup.select('.lyrics')

    text = ''
    for elem in elements:
        for t in elem.select('a, span'):
            t.unwrap()
        if elem:
            elem.smooth()
            text += elem.get_text(strip=True, separator='\n')
    # Remove excess strings and lines
    text = re.sub(r'[\(\[].*?[\)\]]', '', text)
    text = os.linesep.join([s for s in text.splitlines() if s])
    return text


class toneAnalyzer:

	def __init__(self):
		# this is my api key - will prob need to remove this
		self.authenticator = IAMAuthenticator('0Ofl1-c0STFcSn4z7_VnRWo7tXwIpVa0xwKNWMYIy1N1')
		self.tone_analyzer = ToneAnalyzerV3(version='2017-09-21', authenticator=self.authenticator)
		self.tone_analyzer.set_service_url('https://api.us-east.tone-analyzer.watson.cloud.ibm.com')
    	
    
	def analyze_tone(self, lyrics):
		result = self.tone_analyzer.tone({'text': lyrics}, sentences=False).get_result()['document_tone']
		tones = ""
		for dict in result['tones']:
    			tones += (str(dict['tone_name']) + ": " + str(dict['score']) + '\n')
		return tones
		
	def resp_headers(self, lyrics):
		return self.tone_analyzer.tone({'text': lyrics}, sentences=False).get_headers()

	
