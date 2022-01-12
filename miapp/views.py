from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Categoria,Producto
from django.db.models import Q
from miapp.forms import formProducto
from blog.models import Articulo
# Create your views here.

def inicio(request):
    articulos = Articulo.objects.all()[0:1]

    return render(request, 'miapp/index.html',{'articulos': articulos})

def sala(request):

    productos = Producto.objects.order_by('-idProducto')

    productos = Producto.objects.filter(estado=True)

    return render(request,'miapp/sala.html',{'productos': productos})

def sobrenosotros(request): 

    return render(request,"miapp/sobrenosotros.html")

def crear_producto(request,idProducto,nombre,descripcion,artista,estado):
    producto = Producto(
        idProducto = idProducto ,
        nombre = nombre,
        descripcion = descripcion,
        artista = artista,
        estado = estado,
        fechaCrea= '10/02/2009'
    )

    producto.save()
    return HttpResponse(f"Usuario Creado: {producto.idProducto} - {producto.nombre} - {producto.descripcion}")

def producto(request):

    producto = Producto.objects.get(pk=5)

    return HttpResponse(f"Producto: {producto.nombre}")

def editar_producto(request, id): 
    
    producto = Producto.objects.get(pk=id)

    producto.nombre = "Caracas Avila"

    producto.save()

    return HttpResponse(f"Producto Editado: {producto.nombre}")

def borrar_producto(request, id): 
    
    producto = Producto.objects.get(pk=id)
    producto.delete()

    return redirect('sala')

def form_crear_producto(request):

    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    artista = request.POST['artista']
    estado = request.POST['estado']
    fechaCrea = request.POST['fechacrea']
    imagen = request.FILES['imagen']
    if request.method == 'POST':
        producto = Producto(
            nombre = nombre,
            descripcion = descripcion,
            artista = artista,
            estado = estado,
            fechaCrea= fechaCrea,
            imagen = imagen
        )
        producto.save()
        return HttpResponse(f"Usuario Creado: {producto.nombre} - {producto.descripcion} - {producto.artista}")
    else: 
        return HttpResponse("<h2>No se pudo crear el producto</h2>")

def form_producto(request):


    return render(request, 'formu_producto.html')

def form_py_producto(request):

    if request.method == 'POST':
        formulario = formProducto(request.POST)
        
        if formulario.is_valid():

            datos_form = formulario.cleaned_data

            nombre = datos_form.get('nombre')
            descripcion = datos_form.get('descripcion')
            artista = datos_form.get('artista')
            estado = datos_form.get('estado')
            fechaCrea = datos_form.get('fechacrea')

            producto = Producto(
            nombre = nombre,
            descripcion = descripcion,
            artista = artista,
            estado = estado,
            fechaCrea= fechaCrea
            )
            producto.save()
            return HttpResponse(nombre+ ''+descripcion+''+artista+''+estado+''+fechaCrea)
    else:    
        formulario = formProducto()

    return render(request, 'form_py_producto.html', {'form': formulario} )

def verproducto(request, id): 
    
    producto = Producto.objects.get(pk=id)
    

    return render(request, 'ver_producto.html', {'producto': producto})
