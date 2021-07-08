from django import forms
from .models import Proveedor, Usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email","password1","password2"]