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
	User.objects.all().delete()
	Song.objects.all().delete()
	return render(request, 'login.html', {})

def form(request):
	# do upon login #
	# don't attempt to make the User object if it already exists
	# or if we did not log in yet
	try:
		user = request.user
		spot_login = user.social_auth.get(provider='spotify')
		url = "https://api.spotify.com/v1/me"
		headers={'Accept':'application/json', 'Authorization':"Bearer "+ spot_login.extra_data['access_token']}
		r = requests.get(url, headers=headers).content
		data = json.loads(r.decode('utf-8'))
		disp_name = data['display_name']
		user_id = data['id']
		# TODO: don't add a duplicate user
		User.objects.create(name=disp_name, user_id=user_id)
	except:
		pass
	# end do upon login #

	users = User.objects.all()
	songs = Song.objects.all()
	context = {
		'users' : users,
		'songs' : songs
	}
	return render(request, 'form.html', context)

def report(request):
	message = ""
	# don't attempt to do the tone analysis unless we
	# requested it and it hasn't already been done
	try:
		user = request.user
		spot_login = user.social_auth.get(provider='spotify')
		requested_title = request.GET['song-title']
		url = 'https://api.spotify.com/v1/search?q='+requested_title+'&type=track&market=US&limit=1'
		headers={'Accept':'application/json', 'Authorization':"Bearer "+ spot_login.extra_data['access_token']}
		r = requests.get(url, headers=headers).content
		r = json.loads(r.decode('utf-8'))['tracks']['items'][0]['album']['artists'][0]['name']

		# USE GET_LYRICS FUNCTION TO PULL LYRICS
		r = get_lyrics(r, requested_title)
		
		# tone analyzer object 
		analyzer = toneAnalyzer()

		# do tone analysis
		result = analyzer.analyze_tone(r)

		# try to add the analysis to the db
		# if it fails simply move on with no error message 
		# (means it was already in the db)
		try:
			Song.objects.create(title=requested_title.title(), tone=result)
		except:
			message = ""
	# if we came here without requesting, or the analysis failed we enter here
	except:
		# see if we attempted to find a song which wasn't found first
		try:
			if requested_title == '':
		   		message = ""
			else:
				message = "Could not find any song titled " + "\"" + str(requested_title) + "\", please try again!"
		# otherwise we did not request a song
		except:
			message = ""

	users = User.objects.all()
	songs = Song.objects.all()
	context = {
		'users' : users,
		'songs' : songs,
		'message': message
	}

	return render(request, 'report.html', context)

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

	
