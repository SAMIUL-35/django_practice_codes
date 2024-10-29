from django.urls import path
from . import views

urlpatterns = [
   
     path('addmusician/', views.addmusician.as_view(),name='addmusician'),
     path('edit-musician/<int:id>/',views.EditMusician.as_view(), name='edit_musician'), 

   
    
]
