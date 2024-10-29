from django.urls import path
from .views import addalbum, update_album, delete_album

urlpatterns = [
    path('add-album/', addalbum.as_view(), name='addalbum'),
    path('edit-album/<int:id>/', update_album.as_view(), name='edit_album'),
    path('delete-album/<int:id>/', delete_album.as_view(), name='delete_album'),
    
]
