class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session['carrito'] = {}
        self.carrito = carrito

    def agregar_producto(self, producto):
        producto_id = str(producto.id_producto)
        if producto_id not in self.carrito.keys():
            self.carrito[producto_id] = {
                'id_producto': producto.id_producto,
                'nombre': producto.nombre_producto,
                'imagen': producto.imagen,
                'cantidad': 1,
                'precio_unidad': producto.precio_unidad,
                'total': producto.precio_unidad
            }
        else:
            self.carrito[producto_id]['cantidad'] += 1
            self.carrito[producto_id]['total'] = producto.precio_unidad * self.carrito[producto_id]['cantidad']
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def eliminar_producto(self, producto):
        producto_id = str(producto.id_producto)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar_carrito()

    def restar_producto(self, producto):
        producto_id = str(producto.id_producto)
        if producto_id in self.carrito.keys():
            self.carrito[producto_id]['cantidad'] -= 1
            self.carrito[producto_id]['total'] -= producto.precio_unidad
            if self.carrito[producto_id]['cantidad'] <= 0:
                self.eliminar_producto(producto)
            self.guardar_carrito()

    def limpiar_carrito(self):
        self.session['carrito'] = {}
        self.session.modified = True
