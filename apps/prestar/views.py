from django.shortcuts import render, redirect
from apps.prestar.formEjemplar import EjemplarForm
from apps.prestar.formPrestar import PrestarForm
from apps.prestar.formUsuario import UsuarioForm
from apps.prestar.models import Ejemplar, Prestar, Usuario
from django.db.models import Sum
from django.db.models import Count

# Create your views here.

def listprestar(request):
    prestamos = Prestar.objects.all().order_by('id')
    context = {'prestamos': prestamos}
    return render(request, 'prestar/listPrestar.html', context)

def home(request):
    return render(request, 'base/base.html')

def prestarCreate(request):
    if request.method == 'POST':
        form = PrestarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('prestar:listprestar')
    else:
        form = PrestarForm()
    return render(request, 'prestar/prestar_form.html', {'form': form})

def prestarEdit(request, id_prestar):
    
    prestamos = Prestar.objects.get(pk=id_prestar)

    if request.method == 'GET':
        form = PrestarForm(instance=prestamos) #clase que importo desde el archivo formVehiculo.py
    else:
        form =PrestarForm(request.POST, instance=prestamos)
        if form.is_valid():
            form.save()
        
        return redirect('prestar:listprestar')
    return render(request, 'prestar/prestar_form.html', {'form': form}) 

def prestarElim(request, id_prestar):
    
    prestar = Prestar.objects.get(pk=id_prestar)

    if request.method == 'POST':
        prestar.delete() #es que se usa para eliminar un elemento de la base de datos
        return redirect('prestar:listprestar')

    return render(request,'prestar/prestarElimform.html', {'prestamos': prestar})

########## Usuarios ##############

def listUsuario(request):
    usuarios = Usuario.objects.all().order_by('id')
    context = {'usuarios': usuarios}
    return render(request, 'usuarios/listUsuario.html', context)

def usuarioCreate(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('prestar:listUsuario')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/usuario_form.html', {'form': form})

def usuarioEdit(request, id_usuario):
    
    usuarios = Usuario.objects.get(pk=id_usuario)

    if request.method == 'GET':
        form = UsuarioForm(instance=usuarios) #clase que importo desde el archivo formVehiculo.py
    else:
        form =UsuarioForm(request.POST, instance=usuarios)
        if form.is_valid():
            form.save()
        
        return redirect('prestar:listUsuario')
    return render(request, 'usuarios/usuario_form.html', {'form': form})

def usuarioElim(request, id_usuario):
    
    usuario = Usuario.objects.get(pk=id_usuario)

    if request.method == 'POST':
        usuario.delete() #es que se usa para eliminar un elemento de la base de datos
        return redirect('prestar:listUsuario')

    return render(request,'usuarios/usuarioElimform.html', {'usuarios': usuario})


############## Ejemplar #################

def listEjemplar(request):
    ejemplares = Ejemplar.objects.all().order_by('id')
    context = {'ejemplares': ejemplares}
    return render(request, 'ejemplares/listEjemplares.html', context)

def ejemplarCreate(request):
    if request.method == 'POST':
        form = EjemplarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('prestar:listEjemplar')
    else:
        form = EjemplarForm()
    return render(request, 'ejemplares/ejemplar_form.html', {'form': form})

def ejemplarEdit(request, id_ejemplar):
    
    ejemplares = Ejemplar.objects.get(pk=id_ejemplar)

    if request.method == 'GET':
        form = EjemplarForm(instance=ejemplares) #clase que importo desde el archivo formVehiculo.py
    else:
        form =EjemplarForm(request.POST, instance=ejemplares)
        if form.is_valid():
            form.save()
        
        return redirect('prestar:listEjemplar')
    return render(request, 'ejemplares/ejemplar_form.html', {'form': form})

def ejemplarElim(request, id_ejemplar):
    
    ejemplar = Ejemplar.objects.get(pk=id_ejemplar)

    if request.method == 'POST':
        ejemplar.delete() #es que se usa para eliminar un elemento de la base de datos
        return redirect('prestar:listEjemplar')

    return render(request,'ejemplares/ejemplarElimform.html', {'ejemplares': ejemplar})

############### Consultas ####################

def consulta1(request):
    prestamos = Prestar.objects.filter(fechaPres__range=['2022-06-01','2022-08-20']).values('fechaPres','fechaDev','usuario__nombre','ejemplar__localizacion','ejemplar__libro__titulo','ejemplar__libro__autor__nombre')
    print(prestamos.query)
    context = {'prestamos': prestamos}
    return render(request, 'consultas/consulta1.html', context)

def consulta2(request):
    prestamos =  Prestar.objects.filter(fechaPres__range=['2022-06-01','2022-08-20']).values('ejemplar__libro__titulo').annotate(CantidadTotal=Count('ejemplar__libro__titulo'))
    print(prestamos.query)
    context = {'prestamos': prestamos}
    return render(request, 'consultas/consulta2.html', context)

def consulta3(request):
    prestamos =  Prestar.objects.filter(fechaPres__range=['2022-06-01','2022-08-20']).values('usuario__nombre').annotate(CantidadTotal=Count('ejemplar__libro__titulo'))
    print(prestamos.query)
    context = {'prestamos': prestamos}
    return render(request, 'consultas/consulta3.html', context)


