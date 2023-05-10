from django.db import models
from usuario.models import Usuario,Maestrante,Docente
# Create your models here.

class Avance(models.Model):
    id_avance = models.AutoField(primary_key = True)
    maestrante = models.ForeignKey(Maestrante, on_delete=models.CASCADE,blank = True, null = True)
    #docente = models.ForeignKey(Docente, on_delete=models.CASCADE,blank = True, null = True)
    docente = models.CharField('Docente',max_length=400,blank=True,null=True)  
    nombre_docente = models.CharField('Nombre docente',max_length=400,blank=True,null=True) 
    fecha = models.DateField('Fecha de registro', auto_now = True, auto_now_add = False) 
    actividad  = models.CharField('Actividad',max_length=400,blank=True,null=True)     
    obs  = models.TextField('Observaciones',max_length=400,blank=True,null=True)
    obs_ant  = models.CharField('¿ Se mejoraron las observaciones anteriores?',max_length=400,blank=True,null=True)      
    estado_avance = models.BooleanField('Estado', default = True)


    class Meta:
        verbose_name='Avance'
        verbose_name_plural='Avances'

    def __str__(self):
        return "%s "% (self.maestrante)+"%s "% (self.docente)