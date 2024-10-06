from django.shortcuts import render

def about(request):
    return render(request,('sam/about.html'))
def contact(request):
    return render(request,('sam/contact.html'))