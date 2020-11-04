from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
from .models import *
from .forms import CreateUserForm


def home(request):
    return render(request, 'usuarios/home.html')


def registro(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            nombre_nuevo_usuario = form.cleaned_data.get('username')
            messages.success(request, 'Usuario registrado como: ' + nombre_nuevo_usuario)
            return redirect('inicio_sesion')

    context = {'form': form}
    return render(request, 'usuarios/registro.html', context)


def inicio_sesion(request):

    if request == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'usuarios/inicio_sesion.html', context)


def usuarios_data(request):
    users = Usuario.objects.all()

    context = {'users': users}

    return render(request, 'usuarios/usuarios_data.html', context)

