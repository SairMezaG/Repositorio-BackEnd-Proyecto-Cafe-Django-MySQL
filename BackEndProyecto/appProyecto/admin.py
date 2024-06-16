from django.contrib import admin

from appProyecto.models import *

# Register your models here.

#  Esto me permite visualizar en el administrador de Django los modelos generados 
# para su administración.
admin.site.register(LoteCafe)
admin.site.register(Usuario)
admin.site.register(Maquina)
admin.site.register(Seguimiento)
admin.site.register(TipoProceso)
admin.site.register(Variedad)




