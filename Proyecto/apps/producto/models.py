from django.db import models
from django.utils import timezone

# Create your models here.
class ProductoCategoria(models.Model):
    nombre_producto = models.CharField(max_length=50, unique=True)
    descripcion_producto = models.CharField(max_length=200, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Categoría de productos'
        verbose_name_plural = 'Categorías de productos'
        
    def __str__(self):
        return self.nombre_producto
    
    
class Producto(models.Model):
    
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Categoria')
    modelo = models.CharField(max_length=80)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=200, null=True, blank=True, verbose_name='Descripción')
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return f"{self.modelo} - ${self.precio:.2f}"