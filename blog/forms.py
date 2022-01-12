from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormArticulo (forms.ModelForm):

    estado = forms.BooleanField(required=False)
    
    class Meta: 
        model = Articulo
        fields = ["nombre","imagen","artista","descripcion","estado","categorias","fecha_crea"]

        widgets = {
            "fecha_crea": forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):

    class Meta: 
        model = User 
        fields = ['username','first_name', "last_name", "email", "password1", "password2"]