from django.contrib import admin
from .models import Proveedor, Servicio
from .models import Proveedor, Servicio, Usuarios

# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Servicio)
admin.site.register(Usuarios)
