import json
from django.http import HttpResponse
from .models import Producto

# Create your views here.

def agregar(request, *args, **kwargs):
    if request.method == "GET":  
        idproducto = request.GET.get("cada_producto_id")
        valor = request.GET.get("valor")
        print(valor)
        carro = request.session.get("carro")
        idproducto_rec = idproducto[4:] #quita el utn_
        idproducto_rec = int(idproducto_rec)
        el_prod = Producto.objects.get(id=idproducto_rec)
        cantida = int(valor)
        cantida = int(valor) + 1
        print("esta es cantidaaa",cantida)


        # ###########################################
        # ACTUALIZO VARIABLE DE SESSION
        # ###########################################

        carro[idproducto] = cantida
        request.session["carro"] = carro
        # ###########################################
        # FIN
        # ###########################################
        #print(idproducto)
        #print(carro)
        results = []
        data = {}
        data["idproducto"] = str(idproducto)
        data["cantida"] = str(cantida)
        results.append(data)
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)