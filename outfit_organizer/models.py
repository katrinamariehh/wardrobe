from django.db import models

# Create your models here.


class Piece(models.Model):
    CLOTHING_TYPE_CHOICES = (
        ('bottom', 'bottom'),
        ('top', 'top'),
        ('outerwear', 'outerwear'),
        ('dress', 'dress'),
        ('jewelry', 'jewelry'),
        ('shoes', 'shoes')
    )
    image = models.ImageField(upload_to='piece_images')
    color = models.CharField(max_length=15)
    clothing_type = models.CharField(
            max_length=15, choices=CLOTHING_TYPE_CHOICES)
    name = models.CharField(max_length=20)
    long_description = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % self.name


class Season(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return '%s' % self.name


class Outfit(models.Model):
    pieces = models.ManyToManyField(Piece)
    season = models.ManyToManyField(Season)

    def __str__(self):
        items = []
        for piece in self.pieces.all():
            items.append(piece.name)
            return ', '.join(items)
