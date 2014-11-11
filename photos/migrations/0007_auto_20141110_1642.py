# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20141031_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.AddField(
            model_name='post',
            name='medium_photo',
            field=models.ImageField(null=True, upload_to=b'photo_album/medium_size', blank=True),
            preserve_default=True,
        ),
    ]
