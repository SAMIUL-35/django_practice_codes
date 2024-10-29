

from django.views.generic import TemplateView
from album.models import Albummodel 

class home(TemplateView):
  template_name = 'home.html'
  
  def get(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    context['albums'] = Albummodel.objects.all()
    return self.render_to_response(context)
  
  
  