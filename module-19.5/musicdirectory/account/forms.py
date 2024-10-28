

from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms



class RegisterForm(UserCreationForm):
  
  first_name=forms.CharField( max_length=100)
  last_name=forms.CharField( max_length=100)
  email=forms.EmailField( max_length=100)
  
  class Meta:
    model=User
    fields = ['username', 'first_name', 'last_name', 'email'] 
    
class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']