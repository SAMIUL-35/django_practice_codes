

from django.views.generic import TemplateView


class home(TemplateView):
  template_name = 'home.html'
  
  def get(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    context['name']='samiul'
    return self.render_to_response(context)
  
  
  