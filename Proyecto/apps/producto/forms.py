from django import forms
from . import models

class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ProductoCategoria
        fields = '__all__'
        

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = '__all__'
        
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen_producto': forms.FileInput(attrs={'class': 'form-control'}),
            'fecha_de_publicacion': forms.DateInput(attrs={'class': 'form-control'}),
            
        }

class OfertaForms(forms.ModelForm):
    class Meta:
        model = models.Oferta
        fields = '__all__'
        
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'descuento': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_de_publicacion_oferta': forms.DateInput(attrs={'class': 'form-control'}),
        }
       
