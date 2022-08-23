
from tkinter import Widget
from django import forms 
from .models import Prestamos 
import datetime

class createPrestamo(forms.Form):
    dni = forms.CharField(label="DNI",widget=forms.TextInput(attrs={'class': 'form-control'}) ,required=True)
    apellido =forms.CharField(label="Apellido",widget=forms.TextInput(attrs={'class': 'form-control'}), required= True)
    fecha_inicio = forms.DateField(initial=datetime.date.today, widget = forms.HiddenInput())
    PRESTAMO_PERSONAL = "PP"
    PRESTAMO_ESTUDIANTE = "PE"
    PRESTAMO_COMERCIOS = "PC"
    PRESTAMO_HIPOTECARIO= "PH"
    TIPO_PRESTAMO = [
      (PRESTAMO_PERSONAL,"Prestamo_Personal"),
      (PRESTAMO_ESTUDIANTE,"Prestamo_Estudiante"),
      (PRESTAMO_COMERCIOS,"Prestamo_Comercios"),
      (PRESTAMO_HIPOTECARIO, "Prestamo_Hipotecario"),
    ] 
    valor = forms.CharField(label='Valor del prestamo',widget=forms.TextInput(attrs={'class': 'form-control'}), required= True)
    tipo_prestamo = forms.CharField(label=' Tipo de prestamo ',widget=forms.Select(choices=TIPO_PRESTAMO, attrs={'class': 'form-control'}), initial= PRESTAMO_PERSONAL ,required=True)
    estado_prestamo= forms.BooleanField(label= 'Estado',disabled=True,initial= True)
    
   