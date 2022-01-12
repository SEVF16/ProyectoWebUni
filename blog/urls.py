from django.urls import path
from . import views
#from rest_articulo.views import lista_articulo

urlpatterns = [
    path('articulos/', views.articulos, name="articulos"),
    path('categoria/<int:idCategoria>', views.categoria, name="categoria"),
    path('detalle/<int:idProducto>', views.articulosPag, name="detalle"),
    path('agregar/', views.agregar, name="agregar"),
    path('listar/', views.listarArticulos, name="lista"),
    path('modificar/<int:idProducto>', views.modificarArticulos, name="modificar"),
    path('eliminar/<int:idProducto>', views.eliminarArticulos, name="eliminar"),
    path('registro/', views.registro, name="registro"),
    path('usuarios/', views.homeadmin , name="usuarios"), 
   

    
]