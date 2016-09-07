from django.db import models

# Create your models here.

SEASON_CHOICES = (
    ('fall', 'Fall'),
    ('winter', 'Winter'),
    ('spring', 'Spring',),
    ('summer', 'Summer',),
)


class Piece(models.Model):
    CLOTHING_TYPE_CHOICES = (
        ('bottom', 'Bottom'),
        ('top', 'Top'),
        ('outerwear', 'Outerwear'),
        ('dress', 'Dress'),
        ('jewelry', 'Jewelry'),
        ('shoes', 'Shoes')
    )
    image = models.ImageField(upload_to='piece_images')
    color = models.CharField(max_length=15)
    clothing_type = models.CharField(
            max_length=15, choices=CLOTHING_TYPE_CHOICES)
    name = models.CharField(max_length=20)
    long_description = models.CharField(max_length=100)
    pieces = models.ManyToMany(Piece)


class Season(models.Model):
    name = models.CharField(max_length=15)
