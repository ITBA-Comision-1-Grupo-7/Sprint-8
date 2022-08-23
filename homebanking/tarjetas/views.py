from django.shortcuts import render, redirect
from django.urls import reverse
#importamos el modulo donde esta la clase ContactForm

from .forms import TarjetaForm

from .models import Tarjetas



def Tarjeta(request):
    tarjetas_form = TarjetaForm 
    if request.method == "POST":
        tarjetas_form = tarjetas_form(data=request.POST)
        if tarjetas_form.is_valid():
            nameReceived = request.POST.get('name','')           
            emailReceived = request.POST.get('email','')           
            tarjetaReceived = request.POST.get('tarjeta_id','')   
            tarjet = Tarjetas(name=nameReceived,email=emailReceived,tarjeta=tarjetaReceived)
            return render(request,'tarjetas/tarjetas.html',{'enviado': nameReceived})                
    return render(request,'tarjetas/tarjetas.html', {'form':tarjetas_form})

  