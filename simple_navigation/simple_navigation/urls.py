from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('navigation/', include('navigation.urls')),
    path('', views.home),  # Assuming you have a `home` view in your `views.py`
]
