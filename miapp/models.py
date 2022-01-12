from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria= models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto= models.AutoField(auto_created=True, primary_key=True, verbose_name='Id de Producto')
    nombre= models.CharField(max_length=20, verbose_name='Nombre del Producto')
    imagen= models.ImageField(default = 'null', verbose_name='Imagen del Producto', upload_to="productos")
    descripcion=models.TextField(verbose_name='Descripcion del Producto')
    artista= models.CharField(max_length=20, verbose_name='Artista de Producto')
    estado= models.BooleanField(default = 'null',verbose_name='Estado del Producto')
    fechaCrea= models.CharField(max_length=10, verbose_name='Fecha de Creacion')
    def number(self):
        return self.id_producto

    def __str__(self):

        if self.estado:
            publico = "(publicado)"
        else: 
            publico = "(privado)"
        
        return f"{self.nombre} {publico}"

