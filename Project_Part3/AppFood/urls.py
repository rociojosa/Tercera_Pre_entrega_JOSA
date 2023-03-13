from django.urls import path
from AppFood.views import *

urlpatterns = [
    path('', inicio, name="AppFoodInicio"),
    path('cliente', cliente, name= "AppFoodCliente"),
    path('reservas/<nombre>/<numero_reserva>', crear_reserva, name="AppFoodReservas"),
    path('clientePet', cliente_pet , name="AppFoodClientePet"),
]