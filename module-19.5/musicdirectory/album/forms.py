from django import forms
from .models import Albummodel

class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = Albummodel
        fields = "__all__"