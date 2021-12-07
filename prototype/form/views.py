from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import NameForm
import requests
import json
# Create your views here.

def login(request):
	return render(request, 'login.html', {})

def form(request):
	return render(request, 'form.html', {})

def song_title(request):
	data = request.GET['song-title']
	url = 'https://api.spotify.com/v1/search?q='+data+'&type=track&market=US&limit=1'
	headers = {'Accept': 'application.json' 'Content-Type: application/json' , 'Authorization' : 'Bearer BQABCAH6hkMBCsWjxCCWJkQehpeRCYqqU7lzoGNLG6DkM8yHpGu0ypNCI5xqfi6Dr7iSycqyKJzxo1qEE1qo0vQ82-5I4ubEzS-VsrQs1w3DN3s--DTkGZ9h_uOaenqiJTnVkqeTe67zzMhI-Q6UWl7RR6TPvUTv3ZVMCLFjExDMD1wvbv-B50Fyla6aF995mC2s8Nvqnfb0XArJFiyox_-S5KpYEA'}
	r = requests.get(url, headers=headers).content
	r = json.loads(r.decode('utf-8'))['tracks']['items'][0]['album']['artists'][0]['name']
	return render(request, 'song-title.html', {'data':r})

