from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('contactanos/',views.formulario_contacto,name='formulario-enviar'),
    path('contactanos/enviado/',views.formulario_exitoso,name='formulario-enviado'),
    path('carrito/',views.carrito_compras,name='carrito'),
    path('carrito/venta-exitosa/',views.compra_realizada,name='compra-exitosa'),
    path('productos/wow/',views.productos_wow,name='productos-wow'),
    path('productos/tibia/',views.productos_tibia,name='productos-tibia')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)