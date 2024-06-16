from rest_framework import routers

from .api import UsuarioViewSet, MaquinaViewSet, LoteCafeViewSet, TipoProcesoViewSet, DatosViewSet

router = routers.DefaultRouter()

router.register("api/appProyecto/usuario", UsuarioViewSet, "usuario")

router.register("api/appProyecto/loteCafe", LoteCafeViewSet, "loteCafe")

router.register("api/appProyecto/tipoProceso", TipoProcesoViewSet, "tipoProceso")

router.register("api/appProyecto/variedad", LoteCafeViewSet, "variedad")

router.register("api/appProyecto/maquina", MaquinaViewSet, "maquina")

router.register("api/appProyecto/datos", DatosViewSet, "datos")

urlpatterns = router.urls
 

