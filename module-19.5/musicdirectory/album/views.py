from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Albummodel
from .forms import AlbumForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class addalbum(CreateView):
    model = Albummodel
    form_class = AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('home')

class update_album(UpdateView):
    form_class = AlbumForm
    model = Albummodel
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Album updated successfully.')
        return super().form_valid(form)

class delete_album(DeleteView):
    model = Albummodel
    template_name = 'album_delete.html'  
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'  
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Album deleted successfully.')
        return super().delete(request, *args, **kwargs)
