from django import forms 

class ClienteForm(forms.Form):
    nombre = forms.CharField()
    fecha_nacimiento = forms.IntegerField()
    alergias = forms.CharField()

class BusquedaClienteForm(forms.Form):

    nombre = forms.CharField()