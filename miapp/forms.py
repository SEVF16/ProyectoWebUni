from django import forms
from django.forms.widgets import Textarea 

class formProducto(forms.Form):
    nombre = forms.CharField(
        label = "Nombre")
    descripcion = forms.CharField(
        label = "Descripcion   ",
        widget=forms.Textarea)
    artista = forms.CharField(
        label = "artista")
    estado_opcion = [(0,'No')]
    estado = forms.TypedChoiceField(
        choices = estado_opcion)
    fechacrea = forms.CharField(
        label = "fechacrea")