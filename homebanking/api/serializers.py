from .models import Sucursal
from prestamos.models import Prestamos
from cuentas.models import Cuenta

from rest_framework import serializers

from .models import Cliente
from .models import Tarjeta
from .models import Direccion
from .models import Empleado

class SucursalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 
        
class PrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamos
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 

class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 
        
class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 