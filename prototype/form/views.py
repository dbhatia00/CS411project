from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import NameForm

# Create your views here.

def login(request):
	return render(request, 'login.html', {})

def form(request):
	return render(request, 'temp.html', {})

def song_title(request):
	return render(request, 'song-title.html', {})

def get_song_title(request):
	if request.method == 'POST':
		return HttpResponseRedirect('/get_song_title/song-title/')
	return render(request, 'temp.html', {'form': form})
	