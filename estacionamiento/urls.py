"""estacionamiento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appEstacionamiento import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('clientes/', views.listadoClientes, name='listadoClientes'),
    path('agregarCliente/', views.agregarCliente, name='agregarCliente'),
    path('actualizarCliente/<int:id>/', views.actualizarCliente, name='actualizarCliente'),
    path('eliminarCliente/<int:id>/', views.eliminarCliente, name='eliminarCliente'),

    path('vehiculos/', views.listadoVehiculos, name='listadoVehiculos'),
    path('agregarVehiculo/', views.agregarVehiculo, name='agregarVehiculo'),
    path('actualizarVehiculo/<int:id>/', views.actualizarVehiculo, name='actualizarVehiculo'),
    path('eliminarVehiculo/<int:id>/', views.eliminarVehiculo, name='eliminarVehiculo'),

    path('reservas/', views.listadoReservas, name='listadoReservas'),
    path('agregarReserva/', views.agregarReserva, name='agregarReserva'),
    path('actualizarReserva/<int:id>/', views.actualizarReserva, name='actualizarReserva'),
    path('eliminarReserva/<int:id>/', views.eliminarReserva, name='eliminarReserva'),
]
