from django.contrib import admin
from .models import AudioFile
from .models import Playlist

@admin.register(AudioFile, Playlist)
class AudioFileAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'

# Register your models here.
admin.site.register(AudioFile)
admin.site.register(Playlist)
