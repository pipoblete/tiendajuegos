from django.shortcuts import render
from .models import Juego, Categoria

def index(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
    }
    return render(request, 'index.html', context)

def registro(request):
    return render(request, 'registro.html')

def login(request):
    return render(request, 'login.html')

def juegos(request):
    juegos = Juego.objects.all()
    context = {
        'juegos': juegos,
    }
    return render(request, 'juegos.html', context)