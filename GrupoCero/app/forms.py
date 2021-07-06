from django import forms
from .models import Proveedor, Usuarios

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'