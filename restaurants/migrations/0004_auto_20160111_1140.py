# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20160109_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openhours',
            name='restaurant',
            field=models.ForeignKey(related_name='hours', to='restaurants.Restaurant'),
        ),
    ]
