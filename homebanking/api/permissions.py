from rest_framework import permissions
from .models import Cliente
from .models import Empleado

class esEmpleado(permissions.BasePermission):
    def has_permission(self, request, view):
        dni = request.user.username
        
        if Empleado.objects.filter(employee_dni=dni):
            return True
        else:
            return False

class EmpleadoOCliente(permissions.BasePermission):
    def has_permission(self, request, view):
        dni = request.user.username

        
        if Empleado.objects.filter(employee_dni = dni):
            return True
        elif Cliente.objects.filter(customer_dni = dni):
            return True
        else:
            return False
