from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from . import views


#URLS basadas en clases

urlpatterns = [
    path("", views.index, name="index"),
    path("productocategoria/list/", views.ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("productocategoria/create/", staff_member_required(views.ProductoCategoriaCreate.as_view()), name="productocategoria_create"),
    path("productocategoria/delete/<int:pk>", staff_member_required(views.ProductoCategoriaDelete.as_view()), name="productocategoria_delete"),
    path("productocategoria/update/<int:pk>", staff_member_required(views.ProductoCategoriaUpdate.as_view()), name="productocategoria_update"),
    path("productocategoria/detail/<int:pk>", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
    path("producto/create/", staff_member_required(views.ProductoCreate.as_view()), name="producto_create"),
    path("producto/list/", staff_member_required(views.ProductoList.as_view()), name="producto_list"),
    path("producto/detail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),
    path("producto/update/<int:pk>", staff_member_required(views.ProductoUpdate.as_view()), name="producto_update"),
    path("producto/delete/<int:pk>", staff_member_required(views.ProductoDelete.as_view()), name="producto_delete"),
    path("oferta/create/", staff_member_required(views.OfertaCreate.as_view()), name="oferta_create"),
    path("oferta/list/", views.OfertaList.as_view(), name="oferta_list"),
    path("oferta/detail/<int:pk>", views.OfertaDetail.as_view(), name="oferta_detail"),
    path("oferta/update/<int:pk>", staff_member_required(views.OfertaUpdate.as_view()), name="oferta_update"),
    path("oferta/delete/<int:pk>", staff_member_required(views.OfertaDelete.as_view()), name="oferta_delete"),
    path("ofertas", views.ofertas, name="ofertas"),
]



urlpatterns += staticfiles_urlpatterns()















'''

urlpatterns = [
    path("", views.index, name="index"),
    path("producto_categoria_list/", views.producto_categoria_list, name="producto_categoria_list"),
    path("producto_categoria_create/", views.producto_categoria_create, name="producto_categoria_create"),
    path("producto_categoria_delete/<int:id>/", views.producto_categoria_delete, name="producto_categoria_delete"),
    path("producto_categoria_update/<int:id>/", views.producto_categoria_update, name="producto_categoria_update"),
]

urlpatterns += staticfiles_urlpatterns()
'''