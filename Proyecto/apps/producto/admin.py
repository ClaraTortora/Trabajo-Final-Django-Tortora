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
    
#Registrando las apps con modelos
admin.site.register(models.Producto)

    
    