from blog.models import CategoriaArt, Articulo

def get_categorias(request):


    categorias = CategoriaArt.objects.values_list('idCategoria','nombreCategoria')

    return {'categorias': categorias,
            }

def get_articulos(request):


    articulos = Articulo.objects.all()

    return {'articulos': articulos,
            }