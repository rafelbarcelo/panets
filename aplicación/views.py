from django.shortcuts import render
from .models import Persona, Visitas

def lista_alumnos(request):
    pass

def detalle_alumno(request, num_exp):
     # Obtener la lista de todos los alumnos desde la base de datos
    alumnos = Persona.objects.all()

    # Pasar la lista de alumnos al template
    return render(request, 'lista_alumnos.html', {'alumnos': alumnos})

def nueva_visita(request):
    pass

def lista_visitas(request):
    pass