from django.urls import path
from .views import index, registro, login, juegos, agregar_al_carrito, mostrar_carrito

urlpatterns = [
    path('inicio', index, name='inicio'),
    path('registro', registro, name='registro'),
    path('login', login, name='login'),
    path('juegos', juegos, name='juegos'),
    path('juegos/<int:juego_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', mostrar_carrito, name='carrito'),
]