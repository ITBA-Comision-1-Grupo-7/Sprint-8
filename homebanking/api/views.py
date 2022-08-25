from http import client
from django.shortcuts import render
from .serializers import SucursalesSerializer
from .serializers import PrestamosSerializer
from .serializers import SaldoSerializer
from .models import Sucursal
from prestamos.models import Prestamos 
from cuentas.models import Cuenta
from clientes.models import Cliente
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status










class SucursalesLists(APIView):
    def get(self, request):
        sucursales = Sucursal.objects.all()
        serializer = SucursalesSerializer(sucursales, many=True)
        if sucursales:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
class Prestamos(APIView):
    def delete(self, request, pk):
        #Buscamos el prestamos del cliente
        try: 
            prestamos = Prestamos.objects.filter(dni = pk).first()
            #Buscamos el cliente para buscar su cuenta
            cliente = Cliente.objects.filter(customer_DNI = pk).first()
            clienteId = cliente.customer_id
            cuenta = Cuenta.objects.filter(customer_id = clienteId).first()
            cuenta.balance -= prestamos.valor
            prestamos.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except: 
            return Response('Algo fallo', status=status.HTTP_400_BAD_REQUEST)
    
class PrestamoSucursalList(APIView):
    def get(self, request, sucursal_id):
        try:
            clientes = Cliente.objects.filter(branch_id = sucursal_id)
            dnis = []
            for ppl in clientes:
                dnis.append(ppl.customer_DNI)
            losPrestamos = []
            for dni in dnis:
                losPrestamos.extend(list(Prestamos.objects.filter(dni = int(dni))))
            if losPrestamos:
                serializer = PrestamosSerializer(losPrestamos,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response('Algo fallo', status=status.HTTP_400_BAD_REQUEST)




class SaldoDetails(APIView):
    def get(self, request, pk):
        #Buscamos el prestamos del cliente
        try: 
            #Buscamos el cliente para buscar su cuenta
            saldo = Cliente.objects.filter(customer_DNI = pk).first()
            clienteId = saldo.customer_id
            cuenta = Cuenta.objects.filter(customer_id = clienteId).first()
            return Response(cuenta.balance, status=status.HTTP_204_NO_CONTENT)
        except: 
            return Response('Algo fallo', status=status.HTTP_400_BAD_REQUEST)
            