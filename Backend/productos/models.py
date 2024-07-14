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
    descripcion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='images/', null=True)
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto


class Jornada(models.Model):
    id_jornada = models.AutoField(primary_key=True)
    nombre_jornada = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_jornada

class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=100)
    curriculum = models.FileField(upload_to='curriculums/')
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nombres} {self.apellido_paterno}'