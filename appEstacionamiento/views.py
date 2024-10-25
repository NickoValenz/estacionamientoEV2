from django.shortcuts import render, redirect
from appEstacionamiento.models import ClienteEst
from appEstacionamiento.forms import FormCliente

# Create your views here.

def index(request):
    return render(request, 'appEstacionamiento/index.html')

def listadoReservas(request):
    reservas = ClienteEst.objects.all()
    data = {'reservas':reservas}
    return render(request, 'appEstacionamiento/reservas.html', data)

def agregarReserva(request):
    form = FormCliente()
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'appEstacionamiento/agregarReserva.html', data)

def eliminarReserva(request,id):
    reservas = ClienteEst.objects.get(id = id)
    reservas.delete()
    return redirect('/reservas')

def actualizarReserva(request, id):
    reservas = ClienteEst.objects.get(id = id)
    form = FormCliente(instance=reservas)
    if request.method == 'POST':
        form = FormCliente(request.POST, instance=reservas)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'appEstacionamiento/agregarReserva.html', data)