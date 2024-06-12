""" from .models import Operario

from rest_framework import viewsets, permissions

from .serializer import OperarioSerializer

class OperarioViewSet(viewsets.ModelViewSet):
     queryset =  Operario.objects.all()
     permission_classes = [permissions.AllowAny] 
     serializer_class = OperarioSerializer
      """


from rest_framework import viewsets
from .models import Operario  # Importa tu modelo
from .serializer import OperarioSerializer  # Importa tu serializer

class OperarioViewSet(viewsets.ModelViewSet):
    queryset = Operario.objects.all()
    serializer_class = OperarioSerializer
