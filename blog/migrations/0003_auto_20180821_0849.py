# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180814_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='archivo',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='componentes',
            field=models.CharField(max_length=20, choices=[('Procesadores', 'Procesadores'), ('Placa Video', 'Placa Video'), ('Otros', 'Otros')]),
        ),
    ]
