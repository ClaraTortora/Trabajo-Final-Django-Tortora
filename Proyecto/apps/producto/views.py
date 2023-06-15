from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from . import forms, models


# Create your views here.
#-----Modelo Producto - CRUD
def index(request):
    return render (request, 'producto/index.html')

template_name = "producto/index.html"


#CREATE VIEW
class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:index")


#LIST VIEW
class ProductoList(ListView):
    model = models.Producto


#DETAIL VIEW
class ProductoDetail(DetailView):
    model = models.Producto


#UPDATE VIEW
class ProductoUpdate(UpdateView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")
    form_class = forms.ProductoForm


#DELETE VIEW
class ProductoDelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")
    



#-----Modelo Producto Categoría - CRUD


#LISTAR VIEW
class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria
    
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.ProductoCategoria.objects.filter(nombre_producto__icontains=query)
        else:
            object_list = models.ProductoCategoria.objects.all()
        return object_list
    

#CREATE VIEW
class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:index")
    
    
#DELETE VIEW    
class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")


#UPDATE VIEW
class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
    form_class = forms.ProductoCategoriaForm

#DETAIL VIEW
class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
    
    
    
    
#----Modelo Ofertas - CRUD

def ofertas(request):
    return render (request, 'producto/ofertas.html')


#CREATE VIEW
class OfertaCreate(CreateView):
    model = models.Oferta
    form_class = forms.OfertaForms
    success_url = reverse_lazy("producto:oferta_list")


#DETAIL VIEW
class OfertaDetail(DetailView):
    model = models.Oferta


#UPDATE VIEW
class OfertaUpdate(UpdateView):
    model = models.Oferta
    success_url = reverse_lazy("producto:oferta_list")
    form_class = forms.OfertaForms


#DELETE VIEW
class OfertaDelete(DeleteView):
    model = models.Oferta
    success_url = reverse_lazy("producto:oferta_list")


#LIST VIEW
class OfertaList(ListView):
    model = models.Oferta
    


























'''
# Create your views here.
def index(request):
    return render (request, 'producto/index.html')

def producto_categoria_list(request):
    categorias = models.ProductoCategoria.objects.all()
    context = {'categorias':categorias}
    return render (request, 'producto/producto_categoria_list.html', context)

def producto_categoria_create(request):
   if request.method == "POST":
    form = forms.ProductoCategoriaForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('producto:index')
   else:
       form = forms.ProductoCategoriaForm()
   return render (request, 'producto/producto_categoria_create.html', {'form':form})

def producto_categoria_delete(request, id):
    categoria = models.ProductoCategoria.objects.get(id=id)
    if request.method == "POST":
        categoria.delete()
        return redirect('producto:index')
    return render (request, 'producto/producto_categoria_delete.html', {'categoria':categoria})

def producto_categoria_update(request, id):
    categoria = models.ProductoCategoria.objects.get(id=id)
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('producto:index')
    else:
        form = forms.ProductoCategoriaForm(instance=categoria)
    return render(request, 'producto/producto_categoria_update.html', {'form':form})
    
    '''