# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='componentes',
            field=models.CharField(default=1, max_length=20, choices=[(b'Procesadores', b'Procesadores'), (b'Placa Video', b'Placa Video'), (b'Otros', b'Otros')]),
            preserve_default=False,
        ),
    ]
