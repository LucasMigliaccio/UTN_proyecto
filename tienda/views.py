from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from .models import Producto
# Create your views here.

class EjemploTienda(View):
    template= "tienda.html"

    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params ["productos"] = productos

        try:
            request.session["carro"]
        except:
            request.session["carro"] = {}


        return render(request, self.template, params)


class VerImagenes(View): 
    template = "verimagenes.html"

    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"] = productos
        
        return render(request, self.template, params)


def ver_imagen(request, producto_id):
    params={}
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404
    params["producto"] = producto
    
    return render(request, "verimagen.html", params)