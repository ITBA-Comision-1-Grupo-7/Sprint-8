from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Cliente
from login.form import RegistroForm
import sqlite3
import os

# Create your views here.


def Cuenta(request):
    miCliente = Cliente()   
    miCliente.dni = request.user
    miCliente.img='cuentas/img/classic.png'

    sqliteconnection = sqlite3.connect('db.sqlite3')

    dniC=str(miCliente.dni)
    cursor = sqliteconnection.cursor()
    cursor.execute('SELECT customer_name FROM cliente WHERE customer_DNI =' + dniC)
    miCliente.nombre = cursor.fetchall()
    miCliente.nombre = str(miCliente.nombre[0][0])
    cursor.execute('SELECT customer_surname FROM cliente WHERE customer_DNI =' + dniC)
    miCliente.apellido = cursor.fetchall()
    miCliente.apellido = str(miCliente.apellido[0][0])
    cursor.execute('SELECT customer_id FROM cliente WHERE customer_DNI =' + dniC)
    miCliente.idCuenta = cursor.fetchall()
    miCliente.idCuenta = str(miCliente.idCuenta[0][0])
    cursor.execute('SELECT balance FROM cuenta WHERE customer_id =' + miCliente.idCuenta)
    miCliente.balance = cursor.fetchall()
    miCliente.balance = str(miCliente.balance[0][0])
    cursor.execute('SELECT account_type_id FROM cuenta WHERE customer_id =' + miCliente.idCuenta)
    miCliente.tipoCuenta = cursor.fetchall()
    miCliente.tipoCuenta = str(miCliente.tipoCuenta[0][0])
    cursor.execute('SELECT card_number FROM tarjeta WHERE card_id =' + miCliente.idCuenta)
    miCliente.tarjeta = cursor.fetchall()
    miCliente.tarjetaUlt = str(miCliente.tarjeta[0][0])
    miCliente.tarjetaUlt = miCliente.tarjetaUlt[-4:]

    miCliente.balancef=float(miCliente.balance)
    miCliente.balancef=(f"{miCliente.balancef:,.2f}")
    miCliente.balancef=miCliente.balancef.replace(',',' ')
    miCliente.balancef=miCliente.balancef.replace('.',',')
    miCliente.balancef='$ '+ miCliente.balancef


    if miCliente.tipoCuenta == '1':
        miCliente.tipoCuenta = 'Classic'
        miCliente.tcc=True        
    else:
        miCliente.tcc=False
        
    if miCliente.tipoCuenta == '2':
        miCliente.tipoCuenta = 'Gold'
        miCliente.tcg=True
    else:
        miCliente.tcg=False

    if miCliente.tipoCuenta == '3':
        miCliente.tipoCuenta = 'Black'
        miCliente.tcb=True
    else:
        miCliente.tcb=False

    miCliente.nombreCompleto = miCliente.apellido + ', ' + miCliente.nombre

    return render(request, "cuentas/cuentas.html", {'Cliente': miCliente})


