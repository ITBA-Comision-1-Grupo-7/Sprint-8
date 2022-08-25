from .models import Cuenta
from rest_framework import serializers

class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura 
