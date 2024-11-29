from django.shortcuts import render, redirect
from django.views.generic import FormView, View
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserUpdateForm

class UserRegistrationView(FormView):
    """
    Handles user registration.
    """
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        print(form.cleaned_data)  
        user = form.save()  
        login(self.request, user)  
        print(user)  
        return super().form_valid(form)


class UserLoginView(LoginView):
    """
    Handles user login.
    """
    template_name = 'accounts/user_login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(LogoutView):
    """
    Handles user logout.
    """
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')


# class UserBankAccountUpdateView(View):
#     """
#     Allows users to update their account details.
#     """
#     template_name = 'accounts/pass.change.html'

#     def get(self, request):
#         form = UserUpdateForm(instance=request.user)  
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()  # Save the updated user data
#             messages.success(request, 'Your profile has been updated successfully.')  # Add a success message
#             return redirect('profile')  # Redirect to the user's profile page
#         else:
#             messages.error(request, 'Please correct the errors below.')  # Add an error message
#         return render(request, self.template_name, {'form': form})


from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings  

class pass_change(PasswordChangeView):
   
    model = User
    form_class = PasswordChangeForm
    template_name = 'accounts/profile.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        # Send success message
        messages.success(self.request, 'Password changed successfully.')

        # Send email notification
        user_email = self.request.user.email  
        if user_email:
            send_mail(
                subject="Password Changed Successfully",
                message="Your password has been changed successfully. If you did not request this change, please contact support immediately.",
                from_email=settings.DEFAULT_FROM_EMAIL,  
                recipient_list=[user_email],  
                fail_silently=False,
            )
        return super().form_valid(form)
