from django.shortcuts import render
from .models import Pagina
# Create your views here.
def page(request, slug):

    page= Pagina.objects.get(slug=slug)
    if slug == 'sobre-nosotros':

        return render(request, "pages/sobrenosotros.html",{
            "page": page
        })
    return render(request, "pages/page.html",{
        "page": page
    })