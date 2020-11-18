from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('usuarios/', views.usuarios_data, name='usuarios'),
    path('espacios/',views.espacios ,name = 'espacios_trabajo'),
    path('formulario/',views.formulario ,name = 'formulario')
]
