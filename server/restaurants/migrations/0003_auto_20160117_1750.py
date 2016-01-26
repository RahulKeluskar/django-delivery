# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20160117_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='openhours',
            name='restaurant_link',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='openhours',
            name='restaurant',
            field=models.ForeignKey(related_name='open_hours', to='restaurants.Restaurant'),
        ),
    ]
