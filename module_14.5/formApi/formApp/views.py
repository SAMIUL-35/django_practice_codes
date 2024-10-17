from django.shortcuts import render, redirect
from .form import ApForm
from .models import Form
from django.contrib.auth.hashers import make_password  

def home(request):
    return render(request, 'home.html')

def apiForm(request):
    if request.method == 'POST':
        form = ApForm(request.POST)
        if form.is_valid():
            current_form = Form(
                name=form.cleaned_data['name'],  
                email=form.cleaned_data['email'], 
                password=make_password(form.cleaned_data['password']),  
                value=form.cleaned_data['value']
            )
            current_form.save()  
            return redirect('form')  
    else:
        form = ApForm()
    
    return render(request, 'form.html', {'form': form})
