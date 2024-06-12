""" from .models import Operario

from rest_framework import viewsets, permissions

from .serializer import OperarioSerializer

class OperarioViewSet(viewsets.ModelViewSet):
     queryset =  Operario.objects.all()
     permission_classes = [permissions.AllowAny] 
     serializer_class = OperarioSerializer
      """


from rest_framework import viewsets
from .models import *
from .serializer import OperarioSerializer, ProveedorSerializer, SeguimientoSerializer, MaquinaSerializer  

class OperarioViewSet(viewsets.ModelViewSet):
    queryset = Operario.objects.all()
    serializer_class = OperarioSerializer
    

    
class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer



class SeguimientoViewSet(viewsets.ModelViewSet):
    queryset = Seguimiento.objects.all()
    serializer_class = SeguimientoSerializer
    
    
class MaquinaViewSet(viewsets.ModelViewSet):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer    