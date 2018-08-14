# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180814_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagen',
        ),
        migrations.AddField(
            model_name='post',
            name='archivo',
            field=models.FileField(default=1, upload_to=b'documents/'),
            preserve_default=False,
        ),
    ]
