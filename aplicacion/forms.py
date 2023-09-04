from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PlantasForm(forms.Form):
    especie = forms.CharField(max_length=50, required=True)
    genero = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)
    TAMANIOS = (
        (1, "Chico"),
        (2, "Medio"),
        (3, "Grande"),
    )
    tamanio = forms.ChoiceField(label="Tamanio elegido", choices=TAMANIOS, required=True)
    fertilizada = forms.BooleanField()

        
class MacetasForm(forms.Form):
    nombre = forms.CharField(label="Denominacion",max_length=50, required=True) #el required es para que sea obligatorio
    material= forms.CharField(label="Elemento", max_length=50, required=True)
    precio = forms.IntegerField(label="Costo", required=True)


class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)