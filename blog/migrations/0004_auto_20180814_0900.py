# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='precio',
            field=models.IntegerField(),
        ),
    ]