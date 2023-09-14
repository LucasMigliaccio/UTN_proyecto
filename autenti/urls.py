from django.urls import path
from .views import VRegistro, cerrar_sesion, logeo

app_name= 'autenti'

urlpatterns=[
    path("", VRegistro.as_view(), name="registro"),
    path("cerrar-sesion/", cerrar_sesion, name="cerrar_sesion"),
    path("login/", logeo, name="logeo"),
    ]