from django import forms
from .models import Reservas

class ClienteForm(forms.Form):
    nombre = forms.CharField()
    alergias = forms.CharField()
    reserva = forms.IntegerField(min_value=1,max_value=200)

class ReservaClienteForm(forms.Form):
    nombre = forms.CharField()
    fecha = forms.DateField()
    horario = forms.TimeField(widget=forms.TimeInput(format='%I:%M %p'))

    class Meta:
        model = Reservas
        fields = ('fecha', 'horario', 'nombre')

class BusquedaClienteForm(forms.Form):
    nombre = forms.CharField()
    reserva = forms.IntegerField(min_value=1,max_value=200)

class ClientePetForm(forms.Form):
    nombre = forms.CharField()
    reserva = forms.IntegerField(min_value=1,max_value=200)
    tipo_mascota = nombre = forms.CharField()
    nombre_mascota =nombre = forms.CharField()
