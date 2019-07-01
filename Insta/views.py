from django.views.generic import TemplateView
# Create your views here.

class HelloDjango(TemplateView):
    template_name = 'home.html'