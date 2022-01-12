from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class CategoriaArt(models.Model):
    idCategoria= models.AutoField(auto_created=True,primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria

class Articulo(models.Model):
    idProducto= models.AutoField(auto_created=True, primary_key=True, verbose_name='Id de Producto')
    nombre= models.CharField(max_length=150, verbose_name='Nombre del Producto')
    imagen= models.ImageField(default = 'null', verbose_name='Imagen del Producto', upload_to="productos")
    artista= models.CharField(max_length=30, verbose_name='Nombre del Artista')
    descripcion=RichTextField(verbose_name='Descripcion del Producto')
    estado= models.BooleanField(verbose_name='Estado del Producto', null=True)
    categorias = models.ForeignKey(CategoriaArt, verbose_name="Categorias del articulo", on_delete=models.CASCADE)
    fecha_crea= models.DateField(max_length=10, verbose_name='Fecha de Creacion')

    def __str__(self):
        return self.nombre

    def __str__(self):

        if self.estado:
            publico = "(publicado)"
        else: 
            publico = "(privado)"
        
        return f"{self.nombre} {publico}"

