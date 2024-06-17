from rest_framework import routers

""" from .api import UsuarioViewSet, MaquinaViewSet, LoteCafeViewSet, TipoProcesoViewSet, DatosViewSet """
from .api import *
router = routers.DefaultRouter()

router.register("api/usuario", UsuarioViewSet, "usuario")

router.register("api/loteCafe", LoteCafeViewSet, "loteCafe")

router.register("api/tipoProceso", TipoProcesoViewSet, "tipoProceso")

router.register("api/variedad", LoteCafeViewSet, "variedad")

router.register("api/maquina", MaquinaViewSet, "maquina")

router.register("api/datos", DatosViewSet, "datos")

urlpatterns = router.urls
 

