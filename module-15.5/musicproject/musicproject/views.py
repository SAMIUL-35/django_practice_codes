from django.shortcuts import render
from album.models import Album 

def home(request):
    # Get all Album objects
    albums = Album.objects.all()  

    
    return render(request, 'home.html', {'albums': albums})
