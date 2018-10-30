from django.contrib import admin
from .models import AudioFile
from .models import Playlist

# Register your models here.
admin.site.register(AudioFile)
admin.site.register(Playlist)

