from django.contrib import admin
from django.urls import path
from applications.empleado.views import IndexView, PruebaListView, ModeloPruebaListView
from applications.departamento.views import DepartamentoListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', IndexView.as_view()),
    path('lista_empleado/', ModeloPruebaListView.as_view()),
    path('lista_departamento/', DepartamentoListView.as_view()),
]