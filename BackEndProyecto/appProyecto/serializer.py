from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__' 



        
        
class SeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento
        fields = '__all__'         
        
        
        
class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'             



class LoteCafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteCafe
        fields = '__all__' 



class TipoProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProceso
        fields = '__all__'                             



class VariedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variedad
        fields = '__all__'                                     



class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos
        fields = '__all__'         