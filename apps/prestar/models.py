from django.db import models
from apps.libros.models import Libro
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=60)


    def __str__(self):
        return str(self.nombre)

class Ejemplar(models.Model):
    localizacion = models.CharField(max_length=60)
    libro = models.ForeignKey(Libro, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.localizacion)

class Prestar(models.Model):
    fechaDev = models.DateField()
    fechaPres = models.DateField()
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    ejemplar = models.ForeignKey(Ejemplar, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fechaDev)
