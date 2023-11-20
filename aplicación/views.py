from django.shortcuts import render
from .models import Persona, Visitas

def lista_alumnos(request):
    pass

def detalle_alumno(request, num_exp):
    pass
    return render(request, 'aplicación/detalle_alumno.html', {})

def nueva_visita(request):
    pass

def lista_visitas(request):
    pass
