from django.urls import path
from .views import index, artista, artista2, artista3, artista4, artista5, artista6, artistas, esculturas, pinturas, manualidades, nosotros, usuarios

urlpatterns = [
    path('', index, name="index"),
    path('index/', index, name="index"),
    path('artista/', artista, name="artista"),
    path('artista2/', artista2, name="artista2"),
    path('artista3/', artista3, name="artista3"),
    path('artista4/', artista4, name="artista4"),
    path('artista5/', artista5, name="artista5"),
    path('artista6/', artista6, name="artista6"),
    path('artistas/', artistas, name="artistas"),
    path('esculturas/', esculturas, name="esculturas"),
    path('pinturas/', pinturas, name="pinturas"),
    path('manualidades/', manualidades, name="manualidades"),
    path('nosotros/', nosotros, name="nosotros"),
    path('usuarios/', usuarios, name="usuarios")
]

