from django.urls import path
from apps.libros.views import autorCreate, autorEdit, autorElim, libroCreate, libroEdit, libroElim, listAutores, listLibros


app_name= 'libros'
urlpatterns = [
    path('', listLibros, name = 'listLibros'),
    path('nuevol/', libroCreate, name = 'libroCreate'),
    path('actualizarl/<int:id_libro>/', libroEdit, name='libroEdit'),
    path('eliminarl/<int:id_libro>/', libroElim, name='libroElim'),

    ##### Autor #####
    path('autores', listAutores, name = 'listAutores'),
    path('nuevoa/', autorCreate, name = 'autorCreate'),
    path('actualizara/<int:id_autor>/', autorEdit, name='autorEdit'),
    path('eliminara/<int:id_autor>/', autorElim, name='autorElim'),

]