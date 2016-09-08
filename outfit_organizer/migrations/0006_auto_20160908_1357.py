# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfit_organizer', '0005_auto_20160908_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='clothing_type',
            field=models.CharField(choices=[('bottom', 'bottom'), ('top', 'top'), ('outerwear', 'outerwear'), ('dress', 'dress'), ('jewelry', 'jewelry'), ('shoes', 'shoes'), ('accessories', 'accessories'), ('bags', 'bags')], max_length=15),
        ),
    ]
