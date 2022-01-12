from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="index"),
    path('inicio/', views.inicio, name="inicio"),
    path('sala/',views.sala, name="sala"),
    path("nosotros/", views.sobrenosotros, name="nosotros"),
    path('crear-producto/<int:idProducto>/<str:nombre>/<str:descripcion>/<str:artista>/<str:estado>', views.crear_producto, name="crear-producto"),
    path("producto", views.producto, name="producto"),
    path("editar/<int:id>", views.editar_producto, name="editar"),
    path("borrar/<int:id>", views.borrar_producto, name="borrar"),
    path("registrar-producto", views.form_producto, name="registrar-producto"),
    path("form_crear_producto", views.form_crear_producto, name="form_crear_producto"),
    path("formulario-python", views.form_py_producto, name="formulario-py"),
    path("verproducto/<int:id>", views.verproducto, name="verproducto"),
]
