from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def home(request):
    return render(request, 'usuarios/home.html')


def registro(request):
    return render(request, 'usuarios/registro.html')


def usuarios_data(request):
    users = Usuario.objects.all()

    context = {'users': users}

    return render(request, 'usuarios/usuarios_data.html', context)

