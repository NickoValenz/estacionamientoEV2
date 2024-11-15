from django.db import models
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator

#Modelo ClienteEst
class ClienteEst(models.Model):
    nombre = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El nombre solo puede tener letras"
            )
        ]
    )
    apellido = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El apellido solo puede tener letras"
            )
        ]
    )
    rut = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{7,8}-[\dkK]$', message="Rut sin puntos y guion. ")],
        help_text=" (ej.'12345678-9')"
    )
    telefono = models.CharField(
        max_length=9,
        validators=[RegexValidator(regex=r'^\d{9}$', message="El telefono debe contener 9 dígitos.")],
        help_text=" (ej.'912345678')."
    )
    email = models.EmailField(max_length=70)
    direccion = models.CharField(
        max_length=150,
        validators=[
            RegexValidator(
                regex=r'^(?!^\d+$)[a-zA-Z0-9\s]+$',
                message="La direccion debe incluir el nombre y numero de la calle, no solo números."
            )
        ]
    )

    def __str__(self):
        return self.nombre

#modelo a mezclar nico
# 
#Vehiculo
class Vehiculo(models.Model):
    marca = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message="La marca solo debe contener letras y espacios."
            ),
            MaxLengthValidator(20, message="La marca no debe exceder los 20 caracteres.")
        ]
    )
    patente = models.CharField(
        max_length=8,
        validators=[
            RegexValidator(
                regex=r'^[A-Z0-9]+$',
                message="La patente solo puede contener letras mayúsculas y números."
            ),
            MinLengthValidator(6, message="La patente debe tener al menos 6 caracteres."),
            MaxLengthValidator(8, message="La patente no debe exceder los 8 caracteres.")
        ]
    )
    modelo = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9\s]+$',
                message="El modelo solo puede contener letras, numeros y espacios."
            ),
            MaxLengthValidator(50, message="El modelo no debe exceder los 50 caracteres.")
        ]
    )
    color = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message="El color solo puede contener letras y espacios."
            ),
            MaxLengthValidator(50, message="El color no debe exceder los 50 caracteres.")
        ]
    )
    tipo = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message="El tipo solo puede contener letras y espacios."
            ),
            MaxLengthValidator(20, message="El tipo no debe exceder los 20 caracteres.")
        ]
    )

    def __str__(self):
        return f"{self.marca} - {self.patente} - {self.modelo}"

#modelo a mezclar diego
# 
#Reserva
class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('no_activo', 'No Activo'),
    ]

    cliente = models.ForeignKey(ClienteEst, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='activo',
    )

    def __str__(self):
        return f"Reserva de {self.cliente} - Vehículo {self.vehiculo} del {self.fecha_inicio} al {self.fecha_termino} ({self.estado})"
