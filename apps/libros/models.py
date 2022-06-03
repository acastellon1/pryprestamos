from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return str(self.nombre)


class Libro(models.Model):
    titulo = models.CharField(max_length=60)
    noPagina = models.BigIntegerField()
    editorial = models.CharField(max_length=60)
    isbn = models.BigIntegerField()
    autor = models.ForeignKey(Autor, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo)


