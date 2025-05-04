from django.contrib import admin
from atexit import register
from .models import Empleado, Habilidades
import csv
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import date

# Register your models here.
admin.site.register(Habilidades)

def export_selected_to_csv(modeladmin, request, queryset):
    export_selected_to_csv.short_description = "Exportar empleados seleccionados a CSV"

def export_selected_to_pdf(modeladmin, request, queryset):
    export_selected_to_pdf.short_description = "Exportar empleados seleccionados a PDF"

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'email',
        'fecha_nac',
        'calcularEdad',
        'pais',
        'trabajo',
        'departamento',
        'observaciones',
    )

    search_fields = ('apellido', 'nombre')
    list_filter = ('departamento', 'trabajo', 'pais', 'habilidades')
    actions = [export_selected_to_csv, export_selected_to_pdf]
    
    def calcularEdad(self, obj):
        today = date.today()
        age = today.year - obj.fecha_nac.year - ((today.month, today.day) < (obj.fecha_nac.month, obj.fecha_nac.day))
        print(obj)
        return age
    
    calcularEdad.short_description = 'Edad'

admin.site.register(Empleado, EmpleadoAdmin)