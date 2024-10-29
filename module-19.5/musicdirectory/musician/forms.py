from django import forms
from .models import Musicmodel

class MusicForm(forms.ModelForm):
    
    class Meta:
        model = Musicmodel
        fields = "__all__"