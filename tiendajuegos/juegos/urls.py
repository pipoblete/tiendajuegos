from django.urls import path
from .views import index, registro, login, juegos, agregar_juego, eliminar_juego, restar_juego, limpiar_carrito, carritoVer

urlpatterns = [
    path('inicio', index, name='inicio'),
    path('registro', registro, name='registro'),
    path('login', login, name='login'),
    path('juegos', juegos, name='juegos'),
    path('carrito', carritoVer, name='carrito'),

    
    path('agregar_juego/<int:juego_id>/', agregar_juego, name='agregar_juego'),
    path('eliminar/<int:juego_id>/', eliminar_juego, name="Del"),
    path('restar/<int:juego_id>/', restar_juego, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]