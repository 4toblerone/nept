# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='municipality',
            field=models.CharField(default=b'NEPOZNATO', max_length=b'15', choices=[(b'Barajevo', b'Barajevo'), (b'Vozdovac', b'Vozdovac'), (b'Vracar', b'Vracar'), (b'Grocka', b'Grocka'), (b'Zvezdara', b'Zvezdara'), (b'Zemun', b'Zemun'), (b'Lazarevac', b'Lazarevac'), (b'Mladenovac', b'Mladenovac'), (b'Novi Beograd', b'Novi Beograd'), (b'Obrenovac', b'Obrenovac'), (b'Palilula', b'Palilula'), (b'Rakovica', b'Rakovica'), (b'Savski venac', b'Savski venac'), (b'Sopot', b'Sopot'), (b'Stari grad', b'Stari grad'), (b'Surcin', b'Surcin'), (b'Cukarica', b'Cukarica')]),
            preserve_default=True,
        ),
    ]
