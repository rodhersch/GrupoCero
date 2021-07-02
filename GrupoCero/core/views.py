from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def artista(request):
    return render(request, 'core/artista.html')


def artista2(request):
    return render(request, 'core/artista2.html')


def artista3(request):
    return render(request, 'core/artista3.html')


def artista4(request):
    return render(request, 'core/artista4.html')


def artista5(request):
    return render(request, 'core/artista5.html')


def artista6(request):
    return render(request, 'core/artista6.html')


def artistas(request):
    return render(request, 'core/artistas.html')


def esculturas(request):
    return render(request, 'core/esculturas.html')

def pinturas(request):
    return render(request, 'core/pinturas.html')

def manualidades(request):
    return render(request, 'core/manualidades.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def usuarios(request):
    return render(request, 'core/usuarios.html')