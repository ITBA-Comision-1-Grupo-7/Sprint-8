from email.policy import default
from django import forms

class TarjetaForm(forms.Form):
    name = forms.CharField(label="Nombre completo", required=True)
    email = forms.EmailField(label="Email", required=True)
    emaiConfirm = forms.EmailField(label="Confirmacion Email", required=True)
    fecha_de_nacimiento = forms.DateField(label='Fecha de nacimiento:')
    lista=[('3','Debito Classic'),  ('4','Credit Gold'), ('5', 'Credit Black')]
    direccion = forms.CharField(label="Dirección", required=True)
    tarjeta_id= forms.CharField(label='¿Que tipo de tarjeta desea?', widget=forms.Select(choices=lista))