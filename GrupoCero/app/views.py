from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Usuarios
from .forms import ProveedorForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()

    contexto = {
        'proveedores' : proveedores
    }
    return render(request, 'app/listar_proveedores.html', contexto)

def nuevo_proveedor (request):
    data = {
        'form' : ProveedorForm()
    }
    if request.method=='POST':
        formulario = ProveedorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Agregado correctamente")
            return redirect(to="/listar-proveedores/")
        else:
            data["form"] = formulario
    return render(request, 'app/nuevo_proveedor.html', data)

def modificar_proveedor (request,id):
    proveedor =get_object_or_404(Proveedor,rut = id)
    datos = {
        'form' : ProveedorForm(instance=proveedor)
    }
    if request.method=='POST':
        formulario = ProveedorForm(data=request.POST,instance=proveedor,files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="/listar-proveedores/")
        else:
           datos["form"] = formulario
    return render(request, 'app/modificar_proveedor.html', datos)

def registrar(request):

    data= {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Enviado Correctamente")
            return redirect(to="index")
            
        data["form"] = formulario

    return render(request,'registration/registrate.html',data)

def eliminar_proveedor(request,id):
    proveedor = get_object_or_404(Proveedor,rut = id)
    proveedor.delete()
    messages.success(request,"Eliminado correctamente")
    return redirect(to="listar_proveedores")

def index(request):
    return render(request, 'app/index.html')


def artista(request):
    return render(request, 'app/artista.html')


def artista2(request):
    return render(request, 'app/artista2.html')


def artista3(request):
    return render(request, 'app/artista3.html')


def artista4(request):
    return render(request, 'app/artista4.html')


def artista5(request):
    return render(request, 'app/artista5.html')


def artista6(request):
    return render(request, 'app/artista6.html')


def artistas(request):
    return render(request, 'app/artistas.html')


def esculturas(request):
    return render(request, 'app/esculturas.html')

def pinturas(request):
    return render(request, 'app/pinturas.html')

def manualidades(request):
    return render(request, 'app/manualidades.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')

def usuarios(request):
    return render(request, 'app/usuarios.html')

def sesion(request):
    return render(request, 'app/sesion.html')

def registrate(request):
    return render(request, 'app/registrate.html')

def contacto(request):
    return render(request, 'app/contacto.html')


    