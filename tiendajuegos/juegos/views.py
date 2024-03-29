from django.shortcuts import render, redirect
from .models import Juego, Categoria

from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore


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

def agregar_al_carrito(request, juego_id):
    juego = Juego.objects.get(pk=juego_id)
    if 'carrito' not in request.session:
        request.session['carrito'] = {}
    carrito = request.session['carrito']
    if juego_id in carrito:
        carrito[juego_id]['cantidad'] += 1
    else:
        carrito[juego_id] = {'juego': juego, 'cantidad': 1}
    request.session.modified = True
    return redirect('mostrar_carrito')

def mostrar_carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['juego'].precio * item['cantidad'] for item in carrito.values())
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})
