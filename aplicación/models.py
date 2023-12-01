from django.db import models

class Usuario(models.Model):
    NO_REGISTRADO = 'NR'
    REGISTRADO = 'R'
    ADMINISTRADOR = 'A'

    TIPO_USUARIO_CHOICES = [
        (NO_REGISTRADO, 'No registrado'),
        (REGISTRADO, 'Registrado'),
        (ADMINISTRADOR, 'Administrador'),
    ]

    tipo_usuario = models.CharField(
        max_length=2,
        choices=TIPO_USUARIO_CHOICES,
        default=NO_REGISTRADO
    )
    nombre = models.CharField(max_length=255, blank=True, null=True)
    gmail = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    staff = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.get_tipo_usuario_display()} - {self.nombre}'

class Actividad(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    dia = models.CharField(max_length=20)
    hora_inicio = models.IntegerField()
    hora_fin = models.IntegerField()

    def __str__(self):
        return f'{self.titulo} - {self.dia} - {self.hora_inicio}-{self.hora_fin}'