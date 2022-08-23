from ast import Num
from venv import create
from django.shortcuts import render
from .form import createPrestamo
from .models import Prestamos
import sqlite3

from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

#usamos el decorador
# @login_required
def prestamo(request): 
    contact_form = createPrestamo
    todoBien = False

    if request.method == "POST":
        #Traemos los datos enviados
        contact_form = contact_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if contact_form.is_valid():
            dni = request.POST.get('dni')
            apellido = request.POST.get('apellido')
            fecha_inicio = request.POST.get('fecha_inicio')
            tipo_prestamo = request.POST.get('tipo_prestamo')
            estado = request.POST.get('estado_prestamo')
            valor = int(request.POST.get('valor'))
            
            if estado == 'on':
                estado = True
            else:
                estado = False
           
            sqliteconnection = sqlite3.connect('db.sqlite3')
            
            cursor = sqliteconnection.cursor()
            cursor.execute('SELECT customer_id FROM cliente WHERE customer_DNI = ' + dni)
            customer_id = cursor.fetchall()
            customer_id = str(customer_id[0][0])
            cursor.execute('SELECT account_type_id FROM cuenta WHERE customer_id = ' + customer_id)
            account_type = cursor.fetchall()
            account_type= str(account_type[0][0])
            
            if account_type == '1':
                if valor <= 100000:
                    todoBien = True
            elif account_type == '2':
                if valor <= 300000:
                    todoBien = True
            elif account_type == '3':
                if valor <= 500000:
                    todoBien = True
            
            if todoBien:
                prestamo = Prestamos(dni = dni, apellido= apellido ,fecha_inicio= fecha_inicio, tipo_prestamo=tipo_prestamo,estado_prestamo= estado, valor = valor)
                prestamo.save()
            
            return render(request,'prestamos/prestamos.html',{'enviado': apellido, 'flag':todoBien})

    return render(request,'prestamos/prestamos.html',{'form': contact_form(initial={'dni': request.user})})
