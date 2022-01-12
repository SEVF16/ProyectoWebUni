from django.http import request
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from blog.models import Articulo
from .serializers import ArticuloSerializer
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))

def lista_articulo(request):
    """
    Lista todos los articulos
    """
    if request.method == 'GET': 
        articulo = Articulo.objects.all()
        serializer = ArticuloSerializer(articulo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticuloSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_articulo (request,id):
    """
    Get, update o delete
    """
    try: 
        articulo = Articulo.objects.get(idProducto = id)
    except Articulo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticuloSerializer(articulo)
        return Response(serializer.data)
    if request.method == 'PUT':
        data =JSONParser().parse(request)
        serializer = ArticuloSerializer(articulo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        articulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    