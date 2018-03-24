from django.db import models
from Home.settings import MEDIA_ROOT

# Create your models here.


class AudioFile(models.Model):

    class Meta(object):
        verbose_name = u'Audio File'
        verbose_name_plural = u'Audio Files'

    song_id = models.ManyToManyField('Playlist',
        null=True,
        blank=True,
        verbose_name = u'Playlist'
    )

    path = models.FileField(
        upload_to = 'music',
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

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.path, self.name, self.author, self.likes, self.song_id)


class Playlist(models.Model):

    class Meta(object):
        verbose_name = u'Playlist'
        verbose_name_plural = u'Playlists'

    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Playlist name'
        )

    song_id = models.ManyToManyField('AudioFile',
        null=True,
        blank=True,
        verbose_name=u'Songs'
                                      )

    def __unicode__(self):
        return u'%s' % (self.name)

class User():
    pass
