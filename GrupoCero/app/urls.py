from django.urls import path
from .views import index, artista, artista2, artista3, artista4, artista5, artista6, artistas, esculturas, pinturas, manualidades, nosotros, usuarios, sesion, registrate, contacto, listar_proveedores, modificar_proveedor, nuevo_proveedor, eliminar_proveedor, registrar

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
    path('usuarios/', usuarios, name="usuarios"),
    path('sesion/', sesion, name="sesion"),
    path('registrate/', registrate, name="registrate"),
    path('contacto/', contacto, name="contacto"),
    path('listar-proveedores/', listar_proveedores, name="listar_proveedores"),
    path('modificar-proveedor/<id>', modificar_proveedor, name='modificar_proveedor'),
    path('nuevo-proveedor/', nuevo_proveedor, name='nuevo_proveedor'),
    path('eliminar-proveedor/<id>', eliminar_proveedor, name='eliminar_proveedor'),
    path('registrar/', registrar, name='registrar'),
]

