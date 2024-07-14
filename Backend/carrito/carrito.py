class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session['carrito'] = {}
        self.carrito = carrito
        
    def agregar_producto(self, producto):
        if int(producto.id_producto) not in self.carrito.keys():
            self.carrito[producto.id_producto] = {
                'id_producto': producto.id_producto,
                'nombre': producto.nombre_producto,
                'cantidad': 1,
                'total' : int(producto.precio_unidad),  
            }
        else:
            self.carrito[producto.id_producto]['cantidad'] += 1
            self.carrito[producto.id_producto]['total'] += producto.precio_unidad
        self.guardar_carrito()
        
    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True
        
    def eliminar_producto(self, producto):
        producto_id = int(producto.id_producto)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar_carrito()
            
    def restar_producto(self, producto):
        id = (producto.id_producto)
        if id in self.carrito.keys():
            self.carrito[id]['cantidad'] -= 1
            self.carrito[id]['total'] -= producto.precio_unidad
            if self.carrito[id]['cantidad'] <= 0: 
                self.eliminar_producto(producto)
            self.guardar_carrito()
                
    def limpiar_carrito(self):
        self.session['carrito'] = {}
        self.session.modified = True