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
            name='archivo',
            field=models.FileField(default=1, upload_to=b'documents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='componentes',
            field=models.CharField(default=1, max_length=20, choices=[(b'Procesadores', b'Procesadores'), (b'Placa Video', b'Placa Video'), (b'Otros', b'Otros')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='precio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
