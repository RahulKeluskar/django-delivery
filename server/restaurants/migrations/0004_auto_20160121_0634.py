# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20160117_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openhours',
            name='restaurant_link',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(unique=True, null=True),
        ),
    ]
