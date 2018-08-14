# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_componentes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='precio',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
