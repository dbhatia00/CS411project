from django.shortcuts import render

# Create your views here.

def login(request):
	return render(request, 'login.html', {})

def form(request):
	return render(request, 'temp.html', {})
