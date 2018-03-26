from django.contrib import admin
from .models import AudioFile
from .models import Playlist
from .models import PlayListRelations

# Register your models here.
admin.site.register(AudioFile)
admin.site.register(Playlist)
admin.site.register(PlayListRelations)
