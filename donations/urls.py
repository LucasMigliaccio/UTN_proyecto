from django.urls import path
from .views import donation

app_name= 'donations'

urlpatterns=[
    path("",donation, name="donation"),

    ]