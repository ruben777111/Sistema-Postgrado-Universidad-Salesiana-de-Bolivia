from django.contrib import admin
from usuario.models import Cronograma,CentroActividades,Docente_Guia,Docente_Revisor,ActividadesMaestrante,Usuario,Maestrante,TecnicoPostgrado,CoordinacionInvestigacion,CoordinacionPostgrado,Docente
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Maestrante)
admin.site.register(TecnicoPostgrado)
admin.site.register(CoordinacionInvestigacion)
admin.site.register(CoordinacionPostgrado)
admin.site.register(Docente)
admin.site.register(Docente_Guia)
admin.site.register(Docente_Revisor)
admin.site.register(CentroActividades)
admin.site.register(ActividadesMaestrante)
#admin.site.register(Cronograma)

