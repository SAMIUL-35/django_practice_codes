from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .albumform import Albumforms

def Add_album(request):
    if request.method == 'POST':
        form = Albumforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = Albumforms()
    return render(request, 'album.html', {'form': form})

def edit_album(request, id):
    album = get_object_or_404(Album, pk=id)  
    
    if request.method == 'POST':
        form = Albumforms(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Albumforms(instance=album)  

    return render(request, 'album.html', {'form': form})

def delete_album(request, id):
    album = get_object_or_404(Album, pk=id)  
     
    album.delete()
    return redirect('home')
    