from django.shortcuts import render
from AppFood.models import Cliente, Reservas, ClientePet
from AppFood.forms import ClienteForm, BusquedaClienteForm, ReservaClienteForm, ClientePetForm


def buscar_cliente(request):
    mi_formulario = BusquedaClienteForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        clientes_filtrados = Cliente.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "clientes": clientes_filtrados
        }
        return render(request, "AppFood/busqueda_cliente.html", context)
    else:

        return render(request, "AppFood/busqueda_cliente.html")


def inicio(request):
    return render(request, "AppFood/inicio.html")

def clientes(request):
    if request.method == "POST":
        mi_formulario = ClienteForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente_save = Cliente(
                nombre=informacion['nombre'],
                alergias = informacion['alergias'],
                reserva = informacion['reserva'],
              )
            
            cliente_save.save()

    all_clientes =Cliente.objects.all()
    context = {
        "nombre": all_clientes,
        "form": ClienteForm(),
        "form_busqueda": BusquedaClienteForm(),
    }
    return render(request, "AppFood/cliente.html", context)




def crear_cliente(request, nombre, numero_reserva):
    save_reserva= Cliente( nombre=nombre , reserva=int(numero_reserva))
    save_reserva.save()
    context = {
        "nombre": nombre , "reserva": numero_reserva
    }
    return render(request, "AppFood/save_reserva.html", context)


def reservas(request):
    if request.method == "POST":
        mi_formulario = ReservaClienteForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            reserva_save = Reservas(
                nombre= informacion['nombre'],
                fecha = informacion['fecha'],
                horario = informacion['horario'],
              )
            
            reserva_save.save()

    all_reservas =Reservas.objects.all()
    context = {
        "nombre": all_reservas,
        "form": ReservaClienteForm(),
        "form_busqueda": BusquedaClienteForm(),
    }
    return render(request, "AppFood/reservas.html", context)


def cliente_pet(request):
    if request.method == "POST":
        mi_formulario = ClientePetForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            clientepet_save = ClientePet(
                nombre = informacion['nombre'],
                tipo_mascota = informacion['Tipo de mascota'],
                nombre_mascota = informacion ['Nombre de la mascota'],
              )
            
            clientepet_save.save()

    all_clientespet =ClientePet.objects.all()
    context = {
        "nombre": all_clientespet,
        "form": ClientePetForm(),
    }

    return render(request, "AppFood/clientepet.html", context=context)
