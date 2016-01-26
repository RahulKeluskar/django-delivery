# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_restaurant_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='owner',
        ),
    ]
