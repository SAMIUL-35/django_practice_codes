
from . import views
from django.urls import path

urlpatterns = [
    
    path('music/', views.Add_musician ,name='musician'),
]
