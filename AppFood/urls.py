from django.urls import path
from AppFood import views

urlpatterns = [
    path('', views.inicio),
    path('cliente', views.cliente),
    path('reservas/<nombre>/<numero_reserva>', views.crear_reserva),
    path('clientePet', views.cliente_pet),
]