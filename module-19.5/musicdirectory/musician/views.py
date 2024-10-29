from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from .models import Musicmodel
from .forms import MusicForm
from django.urls import reverse_lazy
from django.contrib import messages

class addmusician(CreateView):
    model = Musicmodel
    form_class = MusicForm
    template_name = 'musician.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Optionally, add a success message
        messages.success(self.request, 'Musician added successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Optionally, add an error message
        messages.error(self.request, 'There was an error adding the musician. Please correct the errors.')
        return super().form_invalid(form)
class EditMusician(UpdateView):
    model = Musicmodel
    form_class = MusicForm
    template_name = 'musician.html'  
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, 'Musician updated successfully.')
        return super().form_valid(form)