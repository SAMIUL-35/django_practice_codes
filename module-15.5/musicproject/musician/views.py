
from django.shortcuts import render, get_object_or_404,redirect
from .musicform import musicians
from .models import Musician

def Add_musician(request):

    if request.method =='POST':
        form=musicians(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician')
        
    else:
        form=musicians()
    return render (request,'musician.html',{'form': form})
def edit_musician(request,id):

    
        album = get_object_or_404(Musician, pk=id)  
    
        if request.method == 'POST':
            form = musicians(request.POST, instance=album)
            if form.is_valid():
                form.save()
            return redirect('home')
        else:
            form = musicians(instance=album)  

        return render(request, 'musician.html', {'form': form})