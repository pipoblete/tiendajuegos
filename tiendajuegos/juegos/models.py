from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='juegos/', null=True, blank=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    juego_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre
