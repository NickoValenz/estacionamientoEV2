from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class ClienteEst(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    telefono = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')],
        blank=True,
        null=True
    )
    email = models.EmailField(max_length=70)
    direccion = models.CharField(max_length=150)