from django.db import models

class Tipo(models.Model):
    nombre=models.Charfield(max_lenght=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="TipoProducto"
        verbose_name_plural="TiposProductos"

    def__str__(self):
        return self.nombre

class Producto (models.Model):
    nombre=models.Charfield(max_lenght=50)
    tipo=models.ForeignKey(Tipo, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="gimnasio", null=True, balnk=True)
    precio=models.FloatField()
    stock=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
