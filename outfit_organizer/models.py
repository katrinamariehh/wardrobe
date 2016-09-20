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
            return u'<img class="float-left" src="%s" height="100" width="auto" alt="%s" />' % (self.image.url, self.name)
        except ValueError:
            return u'<p>Piece has no associated image</p>'

    def image_tag_with_name(self):
        try:
            return u'<img class="float-left" src="%s" height="100" width="auto" /><p>%s</p>' % (self.image.url, self.name)
        except ValueError:
            return u'<p>Piece has not associated image</p>'

    image_tag_with_name.short_description = "image tag with name"
    image_tag_with_name.allow_tags = True
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
