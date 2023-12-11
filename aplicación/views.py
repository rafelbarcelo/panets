from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Usuario, Actividad

class IndexView(View):
    def get(self, request):
        usuarios = Usuario.objects.all()
        actividades = Actividad.objects.all()
        context = {
            'usuarios': usuarios,
            'actividades': actividades,
        }
        return render(request, 'index.html', context)

class UsuarioDetailView(View):
    def get(self, request, usuario_id):
        usuario = Usuario.objects.get(pk=usuario_id)
        context = {
            'usuario': usuario,
        }
        return render(request, 'usuario_detail.html', context)

class ActividadDetailView(View):
    def get(self, request, actividad_id):
        actividad = Actividad.objects.get(pk=actividad_id)
        context = {
            'actividad': actividad,
        }
        return render(request, 'actividad_detail.html', context)
