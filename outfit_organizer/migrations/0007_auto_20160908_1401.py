# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfit_organizer', '0006_auto_20160908_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='clothing_type',
            field=models.CharField(choices=[('bottoms', 'bottoms'), ('tops', 'tops'), ('outerwear', 'outerwear'), ('dresses', 'dresses'), ('jewelry', 'jewelry'), ('shoes', 'shoes'), ('accessories', 'accessories'), ('bags', 'bags')], max_length=15),
        ),
    ]
