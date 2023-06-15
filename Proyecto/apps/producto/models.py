from django.db import models
from django.utils import timezone

# Create your models here.
class ProductoCategoria(models.Model):
    nombre_producto = models.CharField(max_length=50, unique=True)
    descripcion_producto = models.CharField(max_length=200, null=True, blank=True, verbose_name='descripción')
    fecha_de_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Categoría de productos'
        verbose_name_plural = 'Categorías de productos'
        
    def __str__(self):
        return self.nombre_producto
    
    
class Producto(models.Model):
    
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Categoria')
    modelo = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=200, null=True, blank=True, verbose_name='Descripción')
    fecha_de_publicacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name='Fecha de publicación')
    imagen_producto = models.ImageField(upload_to="imagenes" ,null=True, blank=True,)


    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return f"{self.modelo} - ${self.precio:.2f}"
    
    
class Oferta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    descuento = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Nuevo precio con descuento')
    fecha_de_publicacion_oferta = models.DateTimeField(default=timezone.now, editable=False, verbose_name='Fecha de publicación de la oferta')
    imagen_oferta = models.ImageField(null=True, blank=True, upload_to="ofertas")
    
    def descuento_oferta(self):
        pass
    
    def __str__(self):
        return f"{self.producto} - ${self.descuento:.2f} {self.imagen_oferta}"