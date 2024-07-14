from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contactanos/',views.formulario_contacto,name='formulario-enviar'),
    path('contactanos/enviado/',views.formulario_exitoso,name='formulario-enviado'),
    path('carrito/',views.carrito_compras,name='carrito'),
    path('carrito/venta-exitosa/',views.compra_realizada,name='compra-exitosa'),
]
