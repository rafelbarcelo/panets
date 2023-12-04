from django.urls import path
from . import views
urlpatterns = [
    path('', views.aplicación_list, name='aplicación_list'),
]