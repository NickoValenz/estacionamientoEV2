from django.shortcuts import render, redirect
from appEstacionamiento.models import ClienteEst, Reserva, Vehiculo
from appEstacionamiento.forms import FormCliente, FormReserva, FormVehiculo

# Página de inicio
def index(request):
    return render(request, 'appEstacionamiento/index.html')

# Vistas de ClienteEst
def listadoClientes(request):
    clientes = ClienteEst.objects.all()
    data = {'clientes': clientes}
    return render(request, 'appEstacionamiento/clientes.html', data)

def agregarCliente(request):
    form = FormCliente()
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadoClientes')
    data = {'form': form}
    return render(request, 'appEstacionamiento/agregarCliente.html', data)

def eliminarCliente(request, id):
    cliente = ClienteEst.objects.get(id=id)
    cliente.delete()
    return redirect('listadoClientes')

def actualizarCliente(request, id):
    cliente = ClienteEst.objects.get(id=id)
    form = FormCliente(instance=cliente)
    if request.method == 'POST':
        form = FormCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listadoClientes')
    data = {'form': form}
    return render(request, 'appEstacionamiento/agregarCliente.html', data)

# Vistas de Vehiculo
def listadoVehiculos(request):
    vehiculos = Vehiculo.objects.all()
    data = {'vehiculos': vehiculos}
    return render(request, 'appEstacionamiento/vehiculos.html', data)

def agregarVehiculo(request):
    form = FormVehiculo()
    if request.method == 'POST':
        form = FormVehiculo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadoVehiculos')
    data = {'form': form}
    return render(request, 'appEstacionamiento/agregarVehiculo.html', data)

def eliminarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    vehiculo.delete()
    return redirect('listadoVehiculos')

def actualizarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    form = FormVehiculo(instance=vehiculo)
    if request.method == 'POST':
        form = FormVehiculo(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('listadoVehiculos')
    data = {'form': form}
    return render(request, 'appEstacionamiento/agregarVehiculo.html', data)

# Vistas de Reserva
def listadoReservas(request):
    reservas = Reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'appEstacionamiento/reservas.html', data)

def agregarReserva(request):
    form = FormReserva()
    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadoReservas')
    data = {'form': form}
    return render(request, 'appEstacionamiento/agregarReserva.html', data)

def eliminarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return redirect('listadoReservas')

def actualizarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    form = FormReserva(instance=reserva)
    if request.method == 'POST':
        form = FormReserva(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('listadoReservas')
    data = {'form': form}
    return render(request, 'appEstacionamiento/agregarReserva.html', data)
