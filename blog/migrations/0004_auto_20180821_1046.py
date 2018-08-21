# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180821_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='archivo',
            field=models.FileField(blank=True, upload_to='documents/', null=True),
        ),
    ]
