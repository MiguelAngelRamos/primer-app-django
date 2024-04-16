from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render
class ProductoView(View):
    ## yo llamo un servicio que me trae informacion de la base de datos
    def get(self,request):
        producto = {
        "precio": 1990990,
        "id": 4,
        "title": "Notebook gamer MSI G565",
        "image": "https://http2.mlstatic.com/D_NQ_NP_817738-MLC44782210434_022021-O.webp"
        }
        return render(request, 'index.html', context=producto)
        #return HttpResponse(content='Producto View - Ready!!!')