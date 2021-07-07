from django import forms
<<<<<<< HEAD
from .models import Proveedor
=======
from .models import Proveedor, Usuarios
>>>>>>> 854fc337b84d02f50086dcf3c6f5c6a577c7a0e7

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

<<<<<<< HEAD
=======
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
>>>>>>> 854fc337b84d02f50086dcf3c6f5c6a577c7a0e7
