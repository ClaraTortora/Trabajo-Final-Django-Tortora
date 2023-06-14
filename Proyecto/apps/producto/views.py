from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from . import forms, models


# Create your views here.
def index(request):
    return render (request, 'producto/index.html')

template_name = "producto/index.html"


class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:index")
    
class ProductoList(ListView):
    model = models.Producto


class ProductoDetail(DetailView):
    model = models.Producto


class ProductoUpdate(UpdateView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")
    form_class = forms.ProductoForm
    
class ProductoDelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")
    








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

class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
    
    
#DETAIL VIEW
#def producto_categoria_detail(request: HttpRequest, pk) -> HttpResponse:
    #categoria = models.ProductoCategoria.objects.get(id=pk)
    #return render(request, "producto/productocategoria_detail.html", {"object": categoria})


    
    
    


























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