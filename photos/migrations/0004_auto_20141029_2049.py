# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_post_municipality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='municipality',
            new_name='city_part',
        ),
    ]
