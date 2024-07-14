from django.urls import path
from . import views
from productos.views import *

urlpatterns = [
    path('agregar/<int:pk>/',agregar_producto,name='agregar-producto'),
    path('restar/<int:pk>/',restar_producto,name='restar-producto'),
    path('eliminar/<int:pk>/',eliminar_producto,name='eliminar-producto'),
    path('limpiar/',limpiar_carrito,name='limpiar-carrito'),
    path('aumentar/<int:pk>/',aumentar_producto,name='aumentar-producto'),
]