# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(default=b'', blank=True)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('availability', models.SmallIntegerField(default=1, choices=[(1, b'All day'), (2, b'Breakfast'), (3, b'Lunch'), (4, b'Dinner'), (5, b'Kids menu')])),
            ],
        ),
        migrations.CreateModel(
            name='OpenHours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_hour', models.SmallIntegerField(null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24)])),
                ('to_hour', models.SmallIntegerField(null=True)),
                ('day', models.SmallIntegerField(null=True, choices=[(1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday'), (7, b'Sunday')])),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('address', models.TextField(default=b'', blank=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('cuisine', models.CharField(default=b'', max_length=100, blank=True, choices=[(b'IND', b'Indian'), (b'CHI', b'Chinese'), (b'USA', b'American'), (b'JPN', b'Japanese'), (b'THL', b'Thai'), (b'KHM', b'Khmer'), (b'VNM', b'Vietnamese'), (b'ITL', b'Italian'), (b'MEX', b'Mexican')])),
                ('price', models.SmallIntegerField(null=True, choices=[(1, b'$'), (2, b'$$'), (3, b'$$$'), (4, b'$$$$')])),
                ('delivers', models.BooleanField(default=True)),
                ('site_url', models.URLField(default=500)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='openhours',
            name='restaurant',
            field=models.ForeignKey(related_name='hours', to='restaurants.Restaurant'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='restaurant',
            field=models.ForeignKey(related_name='menu_item', to='restaurants.Restaurant'),
        ),
    ]
