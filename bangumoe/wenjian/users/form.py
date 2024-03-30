# forms.py

from django import forms
from .models import Anime


class AnimeInfoForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['title', 'episodes', 'director']
