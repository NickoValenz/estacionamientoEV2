from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class ClienteEst(models.Model):
    nombre = models.CharField(max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El nombre solo puede tener letras"
            )
        ])
    apellido = models.CharField(max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El apellido solo puede tener letras"
            )
        ])
    rut = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=70)
    direccion = models.CharField(max_length=150,validators=[
            RegexValidator(
                regex=r'^(?!^\d+$)[a-zA-Z0-9\s]+$',
                message="La direccion debe incluir el nombre y numero de la calle, no solo numeros")])