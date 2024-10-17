from django import forms
from .models import Album
from django.forms.widgets import  DateInput

class Albumforms(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'release_date': DateInput(attrs={'type': 'date'}), 
        }
