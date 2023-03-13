from django.http import HttpResponse
from django.shortcuts import render
from AppFood.models import Cliente

def inicio(request):
    return render(request, "AppFood/inicio.html")

def cliente(request):
    return render(request, "AppCoder/cliente.html")

def crear_reserva(request, nombre, numero_reserva):
    save_reserva= Cliente( nombre=nombre , camada=int(numero_reserva))
    save_reserva.save()
    context = {
        "nombre": nombre , "reserva": numero_reserva
    }
    return render(request, "AppFood/save_reserva.html", context)

def cliente_pet(request):
    return render(request, "AppFood/cliente.pet.html")
