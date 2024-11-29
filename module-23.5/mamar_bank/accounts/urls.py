
from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView,pass_change
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/',pass_change.as_view(), name='profile' ),
    # path('change-password/', pass_change.as_view(), name='change_password'),
]