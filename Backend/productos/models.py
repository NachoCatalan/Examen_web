from django.db import models


class TipoProducto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    desc_tipo_producto = models.CharField(max_length=50)

    def __str__(self):
        return self.desc_tipo_producto

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=30)
    precio_unidad = models.IntegerField()
    imagen = models.ImageField(upload_to='images/', null=True)
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    is_oferta = models.BooleanField(null=True)
    precio_oferta = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre_producto


class Tipo_moneda(models.Model):
    id_tipo_moneda = models.AutoField(primary_key=True)
    tipo_moneda = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_moneda

class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=15)
    tipo_moneda = models.ForeignKey(Tipo_moneda, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_completo}'
    
class Compra_producto(models.Model):
    id_compra = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateField(null=True)
    monto_total = models.IntegerField(null=True)
    
    def __int__(self):
        return {self.id_compra}
    