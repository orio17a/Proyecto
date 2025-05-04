from django.db import models
from applications.departamento.models import Departamento

class Habilidades (models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades de empleado'
        ordering = ['habilidad']
        unique_together = ('habilidad',)

    def __str__(self):
        return self.habilidad

class Empleado (models.Model):
    """ Modelo para la tabla Empleado """

    # Contador
    # Administrativo
    # Desarrollador
    # Analista Funcional
    # Otro

    JOB_CHOICES=(
        ('O','Contador'),
        ('1','Administrativo'),
        ('2','Desarrollador'),
        ('3','Analista Funcional'),
        ('4','Otro'),
    )

    nombre = models.CharField('Nombre', max_length=60)
    apellido = models.CharField('Apellido', max_length=60)
    fecha_nac = models.DateField('Fecha de Nacimiento', blank=False, null=False)
    pais = models.CharField('País', max_length=60, blank=True, null=True)
    trabajo = models.CharField('Puesto', max_length=1, choices= JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    email = models.EmailField('Email', max_length=254, blank=True, null=True)
    observaciones = models.TextField('Observaciones', blank=True, null=True)



    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la Empresa'
        ordering = ['-nombre','apellido']
        unique_together = ('nombre','departamento')

    def __str__(self):
        return self.nombre + ' - ' + self.apellido