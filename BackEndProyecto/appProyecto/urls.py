from rest_framework import routers

from .api import OperarioViewSet

router = routers.DefaultRouter()

router.register("api/appProyecto", OperarioViewSet, "operario")

urlpatterns = router.urls
 

