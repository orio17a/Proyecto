from django.shortcuts import render
from django.views.generic import ListView
from .models import Departamento

# Create your views here.
class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'departamento/lista_departamentos.html'
    context_object_name = 'lista_departamento'
