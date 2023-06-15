from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.ProductoCategoria)

@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre_producto", "descripcion_producto",)
    search_fields = ("nombre_producto",)
    list_filter = ("nombre_producto",)
    ordering = ("nombre_producto",)
    
#Registrando la app Producto
admin.site.register(models.Producto)

#Registrando la app Oferta
admin.site.register(models.Oferta)

    
    