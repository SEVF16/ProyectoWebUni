
from pages.models import Pagina 

def get_pages(request):

    pages = Pagina.objects.filter(estado=True).order_by('order').values_list('idPag','titulo','slug')

    return {'pages': pages}