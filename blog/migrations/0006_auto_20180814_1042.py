# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(upload_to=b'documents/'),
        ),
    ]
