# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0002_auto_20170127_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='path',
            field=models.FileField(upload_to=b''),
        ),
    ]
