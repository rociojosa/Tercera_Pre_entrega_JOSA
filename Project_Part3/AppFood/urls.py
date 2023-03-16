from django.urls import path
from AppFood import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('clientes', views.clientes, name= "Clientes"),
    path('cliente/<nombre>/<reserva>', views.crear_cliente, name= "ClienteCreado"),
    path('buscar_cliente', views.busqueda_cliente, name= "Busqueda_cliente"),
    path('reservas', views.reservas, name="Reservas"),
    path('clientePet', views.cliente_pet , name="ClientePet"),
]