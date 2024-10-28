from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.views.generic import CreateView,UpdateView,TemplateView
from .forms import RegisterForm,ChangeUserForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView



class Register(CreateView):
    
    form_class = RegisterForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Registration'
        return context


class user_login(LoginView):
  template_name = 'registration.html'
  def get_success_url(self):
        return reverse_lazy('profile')
  def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
  def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

class update_user(UpdateView):
   form_class=ChangeUserForm
   model = User 
   template_name = 'update_user.html'
   pk_url_kwarg = 'id'
   success_url = reverse_lazy('profile')
    
    
class profile(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  
        return context

    
  
  
class user_Logout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return redirect('home')