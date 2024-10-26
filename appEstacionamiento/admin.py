from django.contrib import admin
from appEstacionamiento.models import ClienteEst

# Register your models here.

class ClienteEstAdmin(admin.ModelAdmin):
    list_display = [
        'nombre', 'apellido', 'rut', 'telefono', 'email', 'direccion']
    
admin.site.register(ClienteEst, ClienteEstAdmin)