# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('image', models.ImageField(upload_to='piece_images')),
                ('color', models.CharField(max_length=15)),
                ('clothing_type', models.CharField(max_length=15, choices=[('bottom', 'Bottom'), ('top', 'Top'), ('outerwear', 'Outerwear'), ('dress', 'Dress'), ('jewelry', 'Jewelry'), ('shoes', 'Shoes')])),
                ('name', models.CharField(max_length=20)),
                ('long_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='outfit',
            name='pieces',
            field=models.ManyToManyField(to='outfit_organizer.Piece'),
        ),
        migrations.AddField(
            model_name='outfit',
            name='season',
            field=models.ForeignKey(to='outfit_organizer.Season'),
        ),
    ]
