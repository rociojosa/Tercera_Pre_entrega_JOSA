from django.shortcuts import render, redirect
from AppFood.models import Cliente
from AppFood.forms import ClienteForm, BusquedaClienteForm


def busqueda_cliente(request):
    mi_formulario = BusquedaClienteForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        clientes_filtrados = Cliente.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "clientes": clientes_filtrados
        }

        return render(request, "AppFood/busqueda_cliente.html", context= context)


def inicio(request):
    return render(request, "AppFood/inicio.html")

def clientes(request):
    if request.method == "POST":
        mi_formulario = ClienteForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente_save = Cliente(
                nombre=informacion['nombre'],
                alergias = informacion['alergias']
              )
            
            cliente_save.save()
        return redirect(request, "AppFood/clientepet.html")

    all_clientes =Cliente.objects.all()
    context = {
        "nombre": all_clientes ,
        "form": ClienteForm(),
        "form_busqueda": BusquedaClienteForm(),
    }
    return render(request, "AppFood/cliente.html", context=context)


def crear_cliente(request, nombre, numero_reserva):
    save_reserva= Cliente( nombre=nombre , camada=int(numero_reserva))
    save_reserva.save()
    context = {
        "nombre": nombre , "reserva": numero_reserva
    }
    return render(request, "AppFood/save_reserva.html", context)


def reservas(request):
    return render(request, "AppFood/reservas.html")

def cliente_pet(request):
    return render(request, "AppFood/clientepet.html")
