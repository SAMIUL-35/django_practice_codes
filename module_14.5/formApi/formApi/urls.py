from django.contrib import admin
from django.urls import path, include
from formApp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),  # Only define this once
    path('formApp/', include('formApp.urls')),
    path('', home, name='home'),
]
