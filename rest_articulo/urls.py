from django.urls import path
from rest_articulo.views import lista_articulo,detalle_articulo
from rest_articulo.viewslogin import login

urlpatterns = [
    path('lista_artic', lista_articulo, name='lista_artic'),
    path('detalle_artic/<id>', detalle_articulo, name='detalle_artic'),
    path('login', login, name='login'),
]
