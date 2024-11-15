from django.contrib import admin
from appEstacionamiento.models import ClienteEst, Vehiculo, Reserva

# Administración de ClienteEst
class ClienteEstAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'rut', 'telefono', 'email', 'direccion']
    
admin.site.register(ClienteEst, ClienteEstAdmin)

# Administración de Vehiculo
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['marca', 'patente', 'modelo', 'color', 'tipo']

admin.site.register(Vehiculo, VehiculoAdmin)

# Administración de Reserva
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'vehiculo', 'fecha_inicio', 'fecha_termino']
    list_filter = ['estado']  #con esta linea se ve por filtro las reservas

admin.site.register(Reserva, ReservaAdmin)
