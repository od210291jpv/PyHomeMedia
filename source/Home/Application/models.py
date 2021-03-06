from django.db import models
from Home.settings import MEDIA_ROOT

# Create your models here.


class AudioFile(models.Model):

    class Meta(object):
        verbose_name = u'Audio File'
        verbose_name_plural = u'Audio Files'

    path = models.FileField(
        upload_to='music',
        blank=False,
    )

    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Song name'
    )

    author = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Author'
    )

    genre = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u'Genre'
    )

    likes = models.IntegerField(
        blank=False,
        verbose_name=u'Likes amount',
        default=0
    )

    playlist = models.ManyToManyField(
        'Playlist',
        blank=True,
        verbose_name=u'Playlist',
    )

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.path, self.name, self.author, self.likes, self.playlist)


class Playlist(models.Model):

    class Meta(object):
        verbose_name = u'Playlist'
        verbose_name_plural = u'Playlists'

    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Playlist name'
        )

    likes = models.IntegerField(
        blank=False,
        verbose_name=u'Likes amount',
        default=0
    )

    def __unicode__(self):
        return u'%s %s %s' % (self.name, self.songs, self.likes)


