# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20160121_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='availability',
            field=models.SmallIntegerField(default=1, choices=[(1, b'All day'), (2, b'Breakfast'), (3, b'Lunch'), (4, b'Dinner'), (5, b"Kids' menu")]),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(unique=True, max_length=300),
        ),
    ]
