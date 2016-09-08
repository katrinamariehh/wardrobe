# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfit_organizer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outfit',
            name='season',
        ),
        migrations.AddField(
            model_name='outfit',
            name='season',
            field=models.ManyToManyField(to='outfit_organizer.Season'),
        ),
        migrations.AlterField(
            model_name='piece',
            name='clothing_type',
            field=models.CharField(choices=[('bottom', 'bottom'), ('top', 'top'), ('outerwear', 'outerwear'), ('dress', 'dress'), ('jewelry', 'jewelry'), ('shoes', 'shoes')], max_length=15),
        ),
    ]
