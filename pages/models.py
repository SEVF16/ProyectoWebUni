from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Pagina(models.Model):
    idPag= models.AutoField(auto_created=True, primary_key=True, verbose_name='Id de Pagina')
    titulo= models.CharField(max_length=50, verbose_name='Titulo de pagina')
    descripcion=RichTextField(verbose_name='Descripcion del Pagina')
    slug= models.CharField(unique=True, max_length=150, verbose_name='URL AMIGABLE')
    order = models.IntegerField(default=0, verbose_name="Orden de las paginas")
    estado= models.BooleanField(verbose_name='Estado de la pagina')
    def __str__(self):
        return self.titulo