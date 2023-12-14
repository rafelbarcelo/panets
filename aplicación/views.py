from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Usuario, Actividad

def usuarios_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios_list.html', {'usuarios': usuarios} )

def usuario_detalle(request,usuario_id):
    usuario = Usuario.objects.filter(pk=usuario_id)
    actividades = Actividad.objects.filter()
    return render(request, 'usuarios_list.html', {'usuario': usuario} )