# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='price',
            field=models.SmallIntegerField(null=True, choices=[(1, b'$'), (2, b'$$'), (3, b'$$$'), (4, b'$$$$')]),
        ),
    ]
