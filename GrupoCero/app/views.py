from django.shortcuts import render

# Create your views here.

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