# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='binAdded',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bin_id', models.CharField(unique=True, max_length=20)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('longitude', models.DecimalField(max_digits=20, decimal_places=13)),
                ('latitude', models.DecimalField(max_digits=20, decimal_places=13)),
            ],
        ),
        migrations.CreateModel(
            name='binDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_date', models.DateTimeField()),
                ('fill_level', models.DecimalField(max_digits=5, decimal_places=3)),
                ('temperature', models.IntegerField()),
                ('bin_id', models.ForeignKey(to='binDetails.binAdded')),
            ],
        ),
    ]
