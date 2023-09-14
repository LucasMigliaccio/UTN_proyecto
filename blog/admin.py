from django.contrib import admin

from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    search_fields= ["titulo", "categoria","fecha_publicacion"]
    list_display= ["titulo", "categoria", "fecha_publicacion", "autor"]

admin.site.register(Autor)

admin.site.register(Categoria)

admin.site.register(Post, PostAdmin)

admin.site.register(Web)

admin.site.register(RedesSociales)


## CONTACTOAPP
admin.site.register(Contacto)

admin.site.register(Subscriptor)