from django.shortcuts import render,redirect

from .musicform import musicians

def Add_musician(request):

    if request.method =='POST':
        form=musicians(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician')
        
    else:
        form=musicians()
    return render (request,'musician.html',{'form': form})
