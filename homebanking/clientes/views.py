from django.shortcuts import render
from .serializers import ClientesSerializer
from .models import Cliente
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# importamos serializador y modelo
# Create your views here.


class ClienteDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, cliente_id):
        username = request.user
        elUser = User.objects.filter(username = username).first()
        
        if (elUser.is_staff or username.username == str(cliente_id)):
            clientes = Cliente.objects.filter(customer_DNI = cliente_id).first()
            serializer = ClientesSerializer(clientes)
            if clientes:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("no sos staff", status=status.HTTP_404_NOT_FOUND)
            
