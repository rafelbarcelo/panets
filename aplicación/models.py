from django.db import models

class Tipo(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name="TipoProducto"
    verbose_name_plural="TiposProductos"

class Producto (models.Model):
    nombre=models.CharField(max_length=50)
    tipo=models.ForeignKey(Tipo, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="gimnasio", null=True, blank=True)
    precio=models.FloatField()
    stock=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
