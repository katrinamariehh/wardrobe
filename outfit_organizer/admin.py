from django.contrib import admin
from .models import Piece, Season, Outfit


class PieceAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'color', 'clothing_type')
    search_fields= ['name']
    readonly_fields = ('image_tag',)
    list_filter = ('clothing_type',)


admin.site.register(Piece, PieceAdmin)
admin.site.register(Season)
admin.site.register(Outfit)
