from django import forms
from appEstacionamiento.models import ClienteEst
from appEstacionamiento.models import Vehiculo
from appEstacionamiento.models import Reserva

class FormCliente(forms.ModelForm):
    class Meta:
        model = ClienteEst
        fields = '__all__'

class FormVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculo 
        fields = '__all__'

class FormReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'vehiculo', 'fecha_inicio', 'fecha_termino']