from rest_framework import routers

from .api import OperarioViewSet, ProveedorViewSet, SeguimientoViewSet,MaquinaViewSet

router = routers.DefaultRouter()

router.register("api/appProyecto/operario", OperarioViewSet, "operario")

router.register("api/appProyecto/proveedor", ProveedorViewSet, "proveedor")

router.register("api/appProyecto/seguimiento", SeguimientoViewSet, "seguimiento")

router.register("api/appProyecto/maquina", MaquinaViewSet, "maquina")

urlpatterns = router.urls
 

