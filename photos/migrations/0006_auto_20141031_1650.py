# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20141031_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='original_photo',
            field=models.ImageField(null=True, upload_to=b'photo_album/originals', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=b'photo_album/thumbnails', blank=True),
            preserve_default=True,
        ),
    ]
