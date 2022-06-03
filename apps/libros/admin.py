from django.contrib import admin
from apps.libros.models import Autor, Libro
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'noPagina', 'editorial', 'isbn', 'autor')

admin.site.register(Autor)
admin.site.register(Libro, )
