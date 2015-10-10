# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('binDetails', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='binadded',
            options={'verbose_name': 'bin', 'verbose_name_plural': 'bins'},
        ),
    ]
