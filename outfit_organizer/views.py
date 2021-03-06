from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView
from .models import Season, Outfit, Piece, CLOTHING_TYPE_CHOICES
from .forms import OutfitForm


class SeasonListView(ListView):
    # view for seeing all outfits in a season
    model = Season


class SeasonOutfitListView(ListView):
    template_name = 'outfit_organizer/season_outfit_list.html'
    queryset = Outfit.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SeasonOutfitListView, self).get_context_data(**kwargs)
        season_id = self.kwargs.get('pk')
        season = Season.objects.get(pk=season_id)
        context['season'] = season
        context['outfits'] = Outfit.objects.filter(season=season)
        return context


class ClothingTypeSetView(ListView):
    template_name = 'outfit_organizer/clothing_type_set.html'
    queryset = Piece.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ClothingTypeSetView, self).get_context_data(**kwargs)
        piece_type = self.kwargs.get('piece_type')
        context['piece_type'] = piece_type
        return context

    def get_queryset(self):
        piece_type = self.kwargs.get('piece_type')
        return Piece.objects.filter(clothing_type=piece_type).order_by('color')


class ClothingTypeListView(ListView):
    template_name = 'outfit_organizer/clothing_type_list.html'

    def get_queryset(self):
        return [choice[1] for choice in CLOTHING_TYPE_CHOICES]


class PieceListView(ListView):
    model = Piece

    def get_queryset(self):
        return Piece.objects.all().order_by('color')


class PieceDetailView(UpdateView):
    model = Piece
    fields = ['color', 'clothing_type', 'name', 'long_description']
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(PieceDetailView, self).get_context_data(**kwargs)
        piece = Piece.objects.get(pk=self.kwargs['pk'])
        context['piece'] = piece
        return context


class OutfitListView(ListView):
    model = Outfit

    def get_queryset(self):
        return Outfit.objects.all().order_by('-pk')


class OutfitCreationView(FormView):
    form_class = OutfitForm
    template_name = "outfit_organizer/create_outfit.html"

    def get_context_data(self, **kwargs):
        context = super(OutfitCreationView, self).get_context_data(**kwargs)
        clothing_types = [clothing_type[0] for clothing_type in CLOTHING_TYPE_CHOICES]
        for clothing_type in clothing_types:
            context[clothing_type] = [piece.image_tag() for piece in Piece.objects.filter(clothing_type=clothing_type)]
        context['clothing_types'] = clothing_types
        return context


# view for seeing all tops/bottoms/etc.
# view to create a new outfit
