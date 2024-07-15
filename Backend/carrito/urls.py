from django.urls import path
from . import views
from productos.views import *

urlpatterns = [
    path('agregar/<str:pk>/',agregar_producto,name='agregar-producto'),
    path('restar/<str:pk>/',restar_producto,name='restar-producto'),
    path('eliminar/<str:pk>/',eliminar_producto,name='eliminar-producto'),
    path('limpiar/',limpiar_carrito,name='limpiar-carrito'),
    path('aumentar/<str:pk>/',aumentar_producto,name='aumentar-producto'),
]