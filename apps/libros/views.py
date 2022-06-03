from django.shortcuts import render, redirect
from apps.libros.formAutor import AutorForm
from apps.libros.formLibro import LibroForm
from apps.libros.models import Autor, Libro
# Create your views here.



def listLibros(request):
    libros = Libro.objects.all().order_by('id')
    context = {'libros': libros}
    return render(request, 'libros/listLibros.html', context)

def libroCreate(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('libros:listLibros')
    else:
        form = LibroForm()
    return render(request, 'libros/libro_form.html', {'form': form})

def libroEdit(request, id_libro):
    
    libros = Libro.objects.get(pk=id_libro)

    if request.method == 'GET':
        form = LibroForm(instance=libros) #clase que importo desde el archivo formVehiculo.py
    else:
        form =LibroForm(request.POST, instance=libros)
        if form.is_valid():
            form.save()
        
        return redirect('libros:listLibros')
    return render(request, 'libros/libro_form.html', {'form': form}) 

def libroElim(request, id_libro):
    
    libro = Libro.objects.get(pk=id_libro)

    if request.method == 'POST':
        libro.delete() #es que se usa para eliminar un elemento de la base de datos
        return redirect('libros:listLibros')

    return render(request,'libros/libroElimform.html', {'libros': libro})


################# Autor #####################

def listAutores(request):
    autores = Autor.objects.all().order_by('id')
    context = {'autores': autores}
    return render(request, 'autores/listAutores.html', context)

def autorCreate(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('libros:listAutores')
    else:
        form = AutorForm()
    return render(request, 'autores/autor_form.html', {'form': form})

def autorEdit(request, id_autor):
    
    autores = Autor.objects.get(pk=id_autor)

    if request.method == 'GET':
        form = AutorForm(instance=autores) #clase que importo desde el archivo formVehiculo.py
    else:
        form =AutorForm(request.POST, instance=autores)
        if form.is_valid():
            form.save()
        
        return redirect('libros:listAutores')
    return render(request, 'autores/autor_form.html', {'form': form}) 

def autorElim(request, id_autor):
    
    autor = Autor.objects.get(pk=id_autor)

    if request.method == 'POST':
        autor.delete() #es que se usa para eliminar un elemento de la base de datos
        return redirect('libros:listAutores')

    return render(request,'autores/autorElimform.html', {'libros': autor})


