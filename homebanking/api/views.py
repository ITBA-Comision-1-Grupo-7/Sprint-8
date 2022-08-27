from http import client
from urllib import response
from django.shortcuts import render
from .serializers import PrestamosRetSerializer, SucursalesSerializer
from .serializers import PrestamosSerializer
from .serializers import SaldoSerializer
from .models import Sucursal
from prestamos.models import Prestamos
from cuentas.models import Cuenta
from clientes.models import Cliente
from empleados.models import Empleado
from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#KaruCosas
from .serializers import ClienteSerializer
from .serializers import TarjetaSerializer
from .serializers import DireccionSerializer
from .models import Cliente
from .models import Tarjeta
from .models import Direccion
from .models import Empleado
from rest_framework import permissions
from .permissions import esEmpleado
from .permissions import EmpleadoOCliente

class SucursalesLists(APIView):
    def get(self, request):
        sucursales = Sucursal.objects.all()
        serializer = SucursalesSerializer(sucursales, many=True)
        if sucursales:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class Prestamos(APIView):
    def delete(self, request, pk):
        # Buscamos el prestamos del cliente
        try:
            prestamos = Prestamos.objects.filter(dni=pk).first()
            # Buscamos el cliente para buscar su cuenta
            cliente = Cliente.objects.filter(customer_DNI=pk).first()
            clienteId = cliente.customer_id
            cuenta = Cuenta.objects.filter(customer_id=clienteId).first()
            cuenta.balance -= prestamos.valor
            prestamos.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('Algo fallo', status=status.HTTP_400_BAD_REQUEST)


class PrestamoSucursalList(APIView):
    def get(self, request, sucursal_id):
        try:
            clientes = Cliente.objects.filter(branch_id=sucursal_id)
            dnis = []
            for ppl in clientes:
                dnis.append(ppl.customer_DNI)
            losPrestamos = []
            for dni in dnis:
                losPrestamos.extend(
                    list(Prestamos.objects.filter(dni=int(dni))))
            if losPrestamos:
                serializer = PrestamosSerializer(losPrestamos, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response('Algo fallo', status=status.HTTP_400_BAD_REQUEST)


class Create_prestamo(APIView):
    def post(self, request):
        try:
            username = request.user
            if Empleado.objects.filter(employee_dni=username.username):
                serializer = PrestamosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response('Datos incorrectos', status=status.HTTP_400_BAD_REQUEST)
            cliente = Cliente.objects.filter(
                customer_DNI=request.data['dni']).first()
            clienteId = cliente.customer_id
            cuenta = Cuenta.objects.filter(customer_id=clienteId).first()
            cuenta.balance += int(request.data['valor'])
            cuenta.save()
            return Response(serializer.data)
        except:
            return Response('Fallo')


class SaldoDetails(APIView):
    def get(self, request, pk):
        # Buscamos el prestamos del cliente
        try:
            # Buscamos el cliente para buscar su cuenta
            saldo = Cliente.objects.filter(customer_DNI=pk).first()
            clienteId = saldo.customer_id
            cuenta = Cuenta.objects.filter(customer_id=clienteId).first()
            return Response(cuenta.balance, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('Algo fallo', status=status.HTTP_400_BAD_REQUEST)


#KaruCosas
class TarjetasDeCliente(APIView):
    permission_classes = [permissions.IsAuthenticated, esEmpleado]

    def get(self, request, customer_dni):

        cliente = Cliente.objects.filter(customer_dni = customer_dni).values().first()
        customer_id = cliente['customer_id']
        tarjetas = Tarjeta.objects.filter(customer_id=customer_id)
        if tarjetas:
            serializer = TarjetaSerializer(tarjetas,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("no tiene tarjetas asociadas", status=status.HTTP_200_OK)

class CambiarDireccionCliente(APIView):
    permission_classes = [permissions.IsAuthenticated, EmpleadoOCliente]
    
    def put(self, request, customer_dni):
        cliente = Cliente.objects.filter(customer_dni = customer_dni).values().first()
        if cliente:
            if cliente['customer_dni'] == request.user.username or Empleado.objects.filter(employee_dni = request.user.username):
                customer_id = cliente['customer_id']
                direccion = Direccion.objects.filter(customer_id = customer_id).first()
                if direccion:
                    serializer = DireccionSerializer(direccion, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response("No existe esa direccion", status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("Esta no es su informacion. Como cliente no puede acceder a ella a menos que sea su info.", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("no existe un cliente con ese DNI", status=status.HTTP_404_NOT_FOUND)

class PrestamosRetrieve(APIView):
    def get(self, request, reqDNI):
        try:
            Presta = Prestamos.objects.filter(dni = reqDNI).all()
            if not Presta:
                return Response('No hay prestamos sobre este cliente', status=status.HTTP_200_OK)
            else:
                montoPrestamo = sum(i.valor for i in Presta.valor)
                serializer = PrestamosRetSerializer(Presta,many=True)
                respuesta = [serializer.data, 'Monto total: ', montoPrestamo]
                return Response(respuesta,status=status.HTTP_200_OK)
        except: 
            return Response('Algo falló', status=status.HTTP_400_BAD_REQUEST)