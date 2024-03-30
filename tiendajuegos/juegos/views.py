from django.shortcuts import render, redirect

from .Carrito import Carrito
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
    print("juegos:", juegos)  

    return render(request, 'juegos.html', context)

def carritoVer(request):
    productos_en_carrito = Juego.objects.all()
    carrito = Carrito(request)
    total= carrito.calcular_total()
    context = {
        'productos_en_carrito': productos_en_carrito,
        'total': total,
    }
    return render(request, 'carrito.html', context)

def agregar_juego(request, juego_id):
    carrito = Carrito(request)
    juego = Juego.objects.get(juego_id=juego_id)
    carrito.agregar(juego)
    return redirect("juegos")

def eliminar_juego(request, juego_id):
    carrito = Carrito(request)
    juego = Juego.objects.get(juego_id)
    carrito.eliminar(juego)
    return redirect("carrito.html")

def restar_juego(request, juego_id):
    carrito = Carrito(request)
    juego = Juego.objects.get(juego_id)
    carrito.restar(juego)
    return redirect("carrito.html")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("juegos")
