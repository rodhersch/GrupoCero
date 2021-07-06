from django.db import models

# Create your models here.

class Servicio (models.Model):

    id_servicio = models.IntegerField(primary_key=True, verbose_name="ID Servicio")

    nombre_servicio = models.CharField(max_length=50, verbose_name="Servicio")


    def str(self):

        return self.nombre_servicio

class Proveedor (models.Model):

    rut = models.CharField(max_length=13 , primary_key=True, verbose_name="Rut proveedor")

    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    descripcion = models.TextField(max_length=100,verbose_name="Descripcion")

    email = models.CharField(max_length=50, verbose_name="Email")

    telefono = models.CharField(max_length=20, verbose_name="Telefono")

    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def str(self):

        return self.nombre

class Usuarios(models.Model):
    nombre=models.CharField(max_length=50, null = True)
    apellido=models.CharField(max_length=50, null = True)
    email=models.EmailField(null = True)
    contrasenia=models.CharField(max_length=50, null = True)
    comuna=models.CharField(max_length=50, null = True)
