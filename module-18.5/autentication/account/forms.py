from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.forms import UserChangeForm
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True) 
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')  # Fixed the typo here
        help_texts = {
            'password1': 'Enter a strong password with at least 8 characters, including uppercase, lowercase, numbers, and special characters.',
            'password2': 'Confirm your password.',
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class edit_user(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email') 

        
