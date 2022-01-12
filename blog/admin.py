from django.contrib import admin
from .models import CategoriaArt, Articulo
# Register your models here.

admin.site.register(CategoriaArt)
admin.site.register(Articulo)

#class ArticuloAdmin(admin.ModelAdmin):
