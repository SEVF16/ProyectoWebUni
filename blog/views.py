from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import CategoriaArt,Articulo
from .forms import FormArticulo, CustomUserCreationForm
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

def articulos(request):
     
    articulos = Articulo.objects.all()

    return render(request, 'articulos/articulos.html',{'articulos': articulos})

def homeadmin(request):
     
    

    return render(request, 'articulos/homeadmin.html')

def categoria(request, idCategoria):

    categoria = CategoriaArt.objects.get(idCategoria=idCategoria)
    articulos = Articulo.objects.filter(categorias_id = idCategoria )

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(articulos, 12)
        articulos = paginator.page(page)
    except: 
        raise Http404

    return render(request, 'categorias/categoria.html', {'categoria': categoria, 'entity': articulos, 'paginator': paginator})


def articulosPag(request, idProducto):
     
    articulo = Articulo.objects.get(idProducto = idProducto)

    return render(request, 'articulos/detalle.html',{'articulo': articulo})

@permission_required('blog.add_articulo')
def agregar(request):
     
    data = {

         'form':FormArticulo()
    }
    
    if request.method == 'POST': 
        formulario = FormArticulo(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
        else: 

            data["form"] = formulario 
    return render(request, 'articulos/agregar.html', data)

@permission_required('blog.view_articulo')
def listarArticulos(request):
     
    articulos = Articulo.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(articulos, 12)
        articulos = paginator.page(page)
    except: 
        raise Http404

    return render(request, 'articulos/lista2.html',{'entity': articulos, 'paginator': paginator})

@permission_required('blog.change_articulo')
def modificarArticulos(request, idProducto):
    
    articulo = get_object_or_404(Articulo, idProducto = idProducto)


    data = {

        'form': FormArticulo(instance=articulo)
    }

    if request.method == 'POST': 
        formulario = FormArticulo(data=request.POST, instance=articulo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="lista")
        else: 

            data["form"] = formulario 
    
    return render (request, 'articulos/modificar.html',data)

@permission_required('blog.delete_articulo')
def eliminarArticulos(request, idProducto):
    
    articulo = get_object_or_404(Articulo, idProducto = idProducto)

    articulo.delete()

    
    return redirect(to="lista")

def registro(request): 
    data = { 
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            #messages.success(request, 'Te has registrado correctamente')
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)