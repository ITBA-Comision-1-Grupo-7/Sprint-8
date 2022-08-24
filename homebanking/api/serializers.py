from .models import Sucursal
from prestamos.models import Prestamos

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