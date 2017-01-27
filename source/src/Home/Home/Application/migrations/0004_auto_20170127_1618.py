# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0003_auto_20170127_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='path',
            field=models.FileField(upload_to=b'music'),
        ),
    ]
