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
from .serializer import *

class UsuarioViewSet(viewsets.ModelViewSet):    
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    

    

class SeguimientoViewSet(viewsets.ModelViewSet):
    queryset = Seguimiento.objects.all()
    serializer_class = SeguimientoSerializer
    
    
class MaquinaViewSet(viewsets.ModelViewSet):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer    


class LoteCafeViewSet(viewsets.ModelViewSet):
    queryset = LoteCafe.objects.all()
    serializer_class = LoteCafeSerializer        



class TipoProcesoViewSet(viewsets.ModelViewSet):
    queryset = TipoProceso.objects.all()
    serializer_class = TipoProcesoSerializer        




class VariedadViewSet(viewsets.ModelViewSet):
    queryset = Variedad.objects.all()
    serializer_class = VariedadSerializer        



class DatosViewSet(viewsets.ModelViewSet):
    queryset = Datos.objects.all()
    serializer_class = DatosSerializer     