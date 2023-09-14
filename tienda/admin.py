from django.contrib import admin

from .models import Saludos, Producto, CategoriaBebidas
# Register your models here.
    
class SaludosAdmin(admin.ModelAdmin):
    list_display = ["tipo"]

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["tipo"]

class BebidasAdmin(admin.ModelAdmin):
    list_display = ["nombre", "categoria"]

admin.site.register(CategoriaBebidas, CategoriaAdmin)
admin.site.register(Saludos, SaludosAdmin)
admin.site.register(Producto, BebidasAdmin)
