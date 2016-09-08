from django.contrib import admin
from .models import Piece, Season, Outfit


class PieceAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'color', 'clothing_type')


admin.site.register(Piece, PieceAdmin)
admin.site.register(Season)
admin.site.register(Outfit)
