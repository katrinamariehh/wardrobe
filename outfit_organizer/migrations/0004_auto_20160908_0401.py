# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfit_organizer', '0003_auto_20160908_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
