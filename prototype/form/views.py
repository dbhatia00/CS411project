from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from form.models import User, Song
#from .forms import NameForm
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
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
	"""
	cred = SpotifyClientCredentials()
	sp = spotipy.Spotify(client_credentials_manager=cred)
	playlists = sp.user_playlists('spotify')
	
	sp_auth = SpotifyOAuth(scope="user-library-read",client_id='4a1b317eb48c4948ba9924037f6f72ed', client_secret='b9e938375f27472b8c0db8d2dee6b4f5', redirect_uri='127.0.0.01:8000/form/song_title')
	code = requests.get("code","")
	token=sp_auth.get_access_token(code=code)
	print(token)
	data = request.GET['song-title']
	url = 'https://api.spotify.com/v1/search?q='+data+'&type=track&market=US&limit=1'
	headers = {'Accept': 'application.json' 'Content-Type: application/json' , 'Authorization' : 'Bearer BQABCAH6hkMBCsWjxCCWJkQehpeRCYqqU7lzoGNLG6DkM8yHpGu0ypNCI5xqfi6Dr7iSycqyKJzxo1qEE1qo0vQ82-5I4ubEzS-VsrQs1w3DN3s--DTkGZ9h_uOaenqiJTnVkqeTe67zzMhI-Q6UWl7RR6TPvUTv3ZVMCLFjExDMD1wvbv-B50Fyla6aF995mC2s8Nvqnfb0XArJFiyox_-S5KpYEA'}
	r = requests.get(url, headers=headers).content
	r = json.loads(r.decode('utf-8'))['tracks']['items'][0]['album']['artists'][0]['name']
	"""
	return render(request, 'song-title.html', {'data':'ahhh'})

