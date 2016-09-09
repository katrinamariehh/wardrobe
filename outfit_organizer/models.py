from django.db import models

# Create your models here.


CLOTHING_TYPE_CHOICES = (
    ('bottoms', 'bottoms'),
    ('tops', 'tops'),
    ('outerwear', 'outerwear'),
    ('dresses', 'dresses'),
    ('jewelry', 'jewelry'),
    ('shoes', 'shoes'),
    ('accessories', 'accessories'),
    ('bags', 'bags')
)


class Piece(models.Model):
    image = models.ImageField(upload_to='piece_images')
    color = models.CharField(max_length=15, blank=True)
    clothing_type = models.CharField(
            max_length=15, choices=CLOTHING_TYPE_CHOICES)
    name = models.CharField(max_length=30)
    long_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '%s' % self.name

    def image_tag(self):
        try:
            return u'<img src="%s" height="100" width="auto" />' % (self.image.url)
        except ValueError:
            return u'<p>SearchImage has no associated image</p>'
    image_tag.short_description = "image tag"
    image_tag.allow_tags = True


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
