# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import AudioFile, Playlist, PlayListRelations
from Home.settings import PORTAL_URL

# Create your views here.


def show_playlist(request, plid):
    playlist_tracks = PlayListRelations.objects.all().filter(playlist_id=plid)
    return HttpResponse('<h1>playlist id: %s </h1><br> %s <h2></2>' % plid, playlist_tracks)


def playlists(request):
    playlst = Playlist.objects.all()
    return render(request, 'playlists.html', {'playlists': playlst})


def index(request):
    return render(request, 'index_new.html', {'portal_url': PORTAL_URL})


def home(request):
    tracks = AudioFile.objects.all()
    return render(request, 'main.html', {'tracks': tracks, 'portal_url': PORTAL_URL})


def test(request):
    tracks = AudioFile.objects.all()
    return render(request, 'Base.html', {'tracks': tracks, 'portal_url': PORTAL_URL})


def add_audio_file(request):
    track = AudioFile(path='#', name='#', author='#', genre='#', likes='0')
    track.save()
    return HttpResponse('<h1>Done</h1>')
