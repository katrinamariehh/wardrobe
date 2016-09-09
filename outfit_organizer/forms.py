from django import forms
from django.forms import ModelForm
from .models import Outfit, Piece, Season


class OutfitForm(forms.Form):
    CHOICES = (('a', 'A'), ('b', 'B'))
    tops = forms.ModelMultipleChoiceField(
            label="tops",
            queryset=Piece.objects.filter(clothing_type="tops")
        )
    bottoms = forms.ModelMultipleChoiceField(
            label="bottoms",
            queryset=Piece.objects.filter(clothing_type="bottoms")
        )
    outerwear = forms.ModelMultipleChoiceField(
            label="outerwear",
            queryset=Piece.objects.filter(clothing_type="outerwear")
        )
    dresses = forms.ModelMultipleChoiceField(
            label="dresses",
            queryset=Piece.objects.filter(clothing_type="dresses")
        )
    jewelry = forms.ModelMultipleChoiceField(
            label="jewelry",
            queryset=Piece.objects.filter(clothing_type="jewelry")
        )
    shoes = forms.ModelMultipleChoiceField(
            label="shoes",
            queryset=Piece.objects.filter(clothing_type="shoes")
        )
    accessories = forms.ModelMultipleChoiceField(
            label="accessories",
            queryset=Piece.objects.filter(clothing_type="accessories")
        )

    def clean(self):
        cleaned_data = super(OutfitForm, self).clean()
        print(cleaned_data)
        print('here')
