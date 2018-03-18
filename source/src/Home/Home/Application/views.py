# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import AudioFile, Playlist
from Home.settings import PORTAL_URL

# Create your views here.

def showplaylist(request, plid):
    return HttpResponse('<h1>playlist id: %s </h1>' % plid)

def playlists(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists.html', {'playlists': playlists})

def index(request):
    return render(request, 'index_new.html', {'portal_url': PORTAL_URL})

def home(request):
    tracks = AudioFile.objects.all()
    return render(request, 'main.html', {'tracks': tracks, 'portal_url': PORTAL_URL})

def test(request):
    tracks = AudioFile.objects.all()
    return render(request, 'Base.html', {'tracks': tracks, 'portal_url': PORTAL_URL})
