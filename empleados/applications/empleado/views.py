from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Empleado

# Create your views here.
class IndexView(TemplateView):
    template_name= 'empleado/home.html'

class PruebaListView(ListView):
    template_name = 'empleado/lista.html'
    queryset = ['A','B','C']
    context_object_name = 'mi_lista'

class ModeloPruebaListView(ListView):
    model = Empleado
    template_name = "empleado/lista_empleados.html"
    context_object_name = 'lista_empleado'
    