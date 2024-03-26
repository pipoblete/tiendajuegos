from django.urls import path
from .views import index, registro, login

urlpatterns = [
    path('inicio', index, name='inicio'),
    path('registro', registro, name='registro'),
    path('login', login, name='login'),
    
]