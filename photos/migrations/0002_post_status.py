# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, b'Pending'), (1, b'Accepted'), (2, b'NOT_NOW'), (3, b'Rejected')]),
            preserve_default=True,
        ),
    ]
