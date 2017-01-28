# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import AudioFile
from Home.settings import PORTAL_URL

# Create your views here.


def test(request):
    return render(request, 'index.html')

def home(request):
    tracks = AudioFile.objects.all()
    return render(request, 'main.html', {'tracks': tracks, 'portal_url': PORTAL_URL})