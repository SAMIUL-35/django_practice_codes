from django.shortcuts import render, redirect
from account.forms import RegisterForm, edit_user
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

def home(request):
    return render(request, 'home.html')

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            return redirect('home')  
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'type': 'register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  
        if form.is_valid():
            auth_login(request, form.get_user())  
            messages.success(request, 'Login successful')
            return redirect('profile') 
        else:
            messages.error(request, 'Invalid credentials')  
    else:
        form = AuthenticationForm() 

    return render(request, 'register.html', {'form': form, 'type': 'login'})  

    

def profile(request):
    return render(request, 'profile.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')  

def edit_profile(request):
    if request.method == 'POST':
        form = edit_user(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        form = edit_user(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})

def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevent logout after password change
            messages.success(request, 'Your password has been updated successfully.')
            return redirect('home')  # Redirect to home after changing password
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
