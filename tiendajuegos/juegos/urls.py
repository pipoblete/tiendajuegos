from django.urls import path
from .views import index, registro, login, juegos, agregar_juego, eliminar_juego, restar_juego, limpiar_carrito

urlpatterns = [
    path('inicio', index, name='inicio'),
    path('registro', registro, name='registro'),
    path('login', login, name='login'),
    path('juegos', juegos, name='juegos'),

    
    path('agregar/<int:producto_id>/', agregar_juego, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_juego, name="Del"),
    path('restar/<int:producto_id>/', restar_juego, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]