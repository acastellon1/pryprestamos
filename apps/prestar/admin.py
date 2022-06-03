from django.contrib import admin
from apps.prestar.models import Usuario, Prestar, Ejemplar

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Prestar)
admin.site.register(Ejemplar)