from django import forms

class ApForm(forms.Form):
    name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=30, required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)
