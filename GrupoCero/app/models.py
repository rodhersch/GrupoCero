from django.db import models

# Create your models here.

class Servicio (models.Model):

    id_servicio = models.IntegerField(primary_key=True, verbose_name="ID Servicio")

    nombre_servicio = models.CharField(max_length=50, verbose_name="Servicio")


    def __str__(self):

        return self.nombre_servicio

class Proveedor (models.Model):

    rut = models.IntegerField(primary_key=True, verbose_name="Rut proveedor")

    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    descripcion = models.TextField(max_length=100,verbose_name="Descripcion")

    email = models.CharField(max_length=50, verbose_name="Email")

    telefono = models.CharField(max_length=20, verbose_name="Telefono")

    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):

        return self.nombre

<<<<<<< HEAD
=======
class Usuarios(models.Model):
    nombre=models.CharField(max_length=50, null = True)
    apellido=models.CharField(max_length=50, null = True)
    email=models.EmailField(null = True)
    contrasenia=models.CharField(max_length=50, null = True)
    comuna=models.CharField(max_length=50, null = True)
>>>>>>> 854fc337b84d02f50086dcf3c6f5c6a577c7a0e7
