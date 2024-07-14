from django.shortcuts import render, redirect
from .forms import *
from carrito.carrito import Carrito

# Create your views here.

def index(request):
    productos = Producto.objects.all()
    context={'productos':productos}
    return render(request,'index.html',context)

def carrito_compras(request):
    context={}
    return render(request,'carrito_compra.html',context)

def agregar_producto(request, pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=pk)
    carrito.agregar_producto(producto)
    return redirect('index')

def aumentar_producto(request, pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=pk)
    carrito.agregar_producto(producto)
    return redirect('carrito')

def restar_producto(request, pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=pk)
    carrito.restar_producto(producto)
    return redirect('carrito')

def eliminar_producto(request, pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto = pk)
    carrito.eliminar_producto(producto)
    return redirect('carrito')    

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar_carrito()
    return redirect('index')

def formulario_contacto(request):
    if request.method == 'POST':
        form = (request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('formulario-enviado') 
    else:
        form = ContactoForm()
    context = {
        'form': form
    }
    return render(request,'formulario_contacto.html',context)

def compra_realizada(request):
    context={}
    return render(request,'compra_realizada.html',context)

def formulario_exitoso(request):
    context={}
    return render(request,'formulario_exitoso.html',context)