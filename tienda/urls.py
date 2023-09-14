from django.urls import path
from .views import EjemploTienda, VerImagenes, ver_imagen
#from .views_agregar import agregar

app_name= 'tienda'

urlpatterns=[
    path("", EjemploTienda.as_view(), name="ejemplo_tienda"),
    path('verimagenes/', VerImagenes.as_view(), name="verimagenes"),
    path('<int:producto_id>/ver/', ver_imagen, name="ver"),
    ]