@@ -1,22 +1,12 @@
"""
URL configuration for mysite project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import lista_alumnos, detalle_alumno, nueva_visita, lista_visitas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumnos/', lista_alumnos, name='lista_alumnos'),
    path('alumnos/<int:num_exp>/', detalle_alumno, name='detalle_alumno'),
    path('visitas/nueva/', nueva_visita, name='nueva_visita'),
    path('visitas/', lista_visitas, name='lista_visitas'),
]

