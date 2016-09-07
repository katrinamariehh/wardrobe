from django.contrib import admin
from .models import Piece

class PieceDisplay(admin.ModelAdmin):
    list_display = ('image', 'color', 'clothing_type')
