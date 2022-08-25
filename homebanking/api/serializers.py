from .models import Sucursal
from prestamos.models import Prestamos
from cuentas.models import Cuenta

from rest_framework import serializers

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