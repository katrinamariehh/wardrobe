# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfit_organizer', '0002_auto_20160908_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='color',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='piece',
            name='long_description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
