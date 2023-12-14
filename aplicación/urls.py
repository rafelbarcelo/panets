from django.urls import path
from . import views
urlpatterns = [
    path('', views.usuarios_list, name='aplicación_list'),
]