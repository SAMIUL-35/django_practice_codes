from . import views
from django.urls import path

urlpatterns = [
    
    path('album/', views.Add_album ,name='album'),
    path('edit/<int:id>', views.edit_album ,name='edit'),
    path('delete/<int:id>', views.delete_album ,name='delete'),
]
