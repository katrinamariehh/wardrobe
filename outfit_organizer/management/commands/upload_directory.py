import os
from django.core.management.base import BaseCommand
from django.core.files import File
from outfit_organizer.models import (Piece, Season, Outfit,
                                     CLOTHING_TYPE_CHOICES)


class Command(BaseCommand):
    help = 'Upload files in a directory as wardrobe pieces'

    def add_arguments(self, parser):
        parser.add_argument('clothing_type')
        parser.add_argument('directory')

    def handle(self, *args, **options):
        clothing_type = options['clothing_type']
        directory = options['directory']
        for image_file in os.listdir(directory):
            filename, ext = image_file.split('.')
            name = filename.replace('_', ' ')
            if ext == 'jpg':
                open_file = open(os.path.join(directory, image_file), 'rb')
                django_file = File(open_file)
                print(name)
                piece = Piece(image=django_file,
                              clothing_type=clothing_type,
                              name=name)
                piece.save()
