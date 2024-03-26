from django.db import models

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='juegos/', null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
