from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import NameForm
import requests
# Create your views here.

def login(request):
	return render(request, 'login.html', {})

def form(request):
	return render(request, 'temp.html', {})

def song_title(request):
	data = request.GET['song-title']
	url = 'https://api.spotify.com/v1/search?q='+data+'&type=track&market=US&limit=1'
	headers = {'Accept': 'application.json' 'Content-Type: application/json' , 'Authorization' : 'Bearer BQC-1tz0RRnnHpa8HYLFsjA4fB1LykSoV0da9xHY4_sWvmjLqjogMfvp49GvlFxACJBuRsjniUoCc-rLgkGqdIGu96bCS16syk1xX0hVRKIt2hzu_quoMcbWjmuqX03Y0FkK9DC85ZKuk_PUFiL-yFSb9uvIAZZRw5Q'}
	r = requests.get(url, headers=headers).content
	return render(request, 'song-title.html', {'data':r})

	
