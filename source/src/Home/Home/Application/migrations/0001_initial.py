# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.FileField(upload_to=b'/media/')),
                ('name', models.CharField(max_length=256, verbose_name='Song name')),
                ('author', models.CharField(max_length=256, verbose_name='Author')),
                ('genre', models.CharField(max_length=256, verbose_name='Genre', blank=True)),
            ],
            options={
                'verbose_name': 'Audio File',
                'verbose_name_plural': 'Audio Files',
            },
        ),
    ]
