from django.urls import path
from .views import index

urlpatterns = [
    path('juegos', index, name='juegos')
]