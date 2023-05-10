from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db.models.signals import post_save,pre_save
# Create your models here.
usuario_tipo=[
    
    (1,'Maestrante'),
    (2,'Docente'),    
    (3,'Tecnico de Postgrado'),
    (4,'Coordonación de investigación'),
    (5,'Coordonación de Postgrado'),
    (6,'Administrador')
]
departamentos=(
    
    ('La Paz','La Paz'),
    ('Cochabamba','Cochabamba'),
    ('Santa Cruz','Santa Cruz'),
    ('Potosi','Potosi'),
    ('Oruro','Oruro'),
    ('Chuquisaca','Chuquisaca'),
    ('Pando','Pando'),
    ('Beni','Beni'),
    ('Tarija','Tarija')
)
class UsuarioManager(BaseUserManager):
    def create_user(self,username,nombre_usuario,password=None):

        user = self.model(
            username=username,
            nombre_usuario=nombre_usuario,
            
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,nombre_usuario,password):
        user=self.create_user(
            
            username=username,
            nombre_usuario=nombre_usuario,
            password=password
        )
        user.usuario_administrador=True
        user.save()
        return user

class Usuario(AbstractBaseUser):
    
    username = models.CharField('Usuario', unique=True,max_length=100)
    ci_usuario = models.IntegerField( blank = False, null = True)
    departamento = models.CharField('Departamento',max_length=200,blank=True,null=True,choices=departamentos)
    nombre_usuario = models.CharField('Nombre',max_length=200,blank=True,null=True)
    
    paterno = models.CharField('Apellido Paterno',max_length=200,blank=True,null=True)
    materno = models.CharField('Apellido Materno',max_length=200,blank=True,null=True)
    
    cel_usuario = models.IntegerField( blank = False, null = True)
    cel_usuario2 = models.IntegerField( blank = False, null = True)
    correo = models.CharField('Correo',max_length=240,blank=True,null=True)
    descripcion = models.CharField('Especialidad',max_length=200,blank=True,null=True)
    imagen_usuario = models.ImageField('Imagen de perfil',upload_to='tesis/',height_field=None,width_field=None,max_length=200,blank = True, null = True)
    usuario_activo = models.BooleanField(default = True)

    usuario_administrador = models.BooleanField(default = False)
    superusuario_administrador = models.BooleanField(default=False)
    fecha_registro = models.DateField('Fecha de registro', auto_now = True, auto_now_add = False)       
    tipo_usuario = models.IntegerField(blank = True, null = True,choices=usuario_tipo)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre_usuario']

    def has_perm(self,perm,ob=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.usuario_administrador

    @property
    def is_superuser(self):
        return self.superusuario_administrador

class Docente(models.Model):
    id_docente = models.AutoField(primary_key = True)
    especialidad_docente = models.CharField(max_length = 220, blank = True, null = True)    
    user = models.OneToOneField(Usuario,on_delete=models.CASCADE,blank = True, null = True)
    guia = models.BooleanField(default = False)
    tribunal = models.BooleanField(default = False)
    revisor = models.BooleanField(default = False)
    class Meta:
        verbose_name='Docente'
        verbose_name_plural='Docentes'

    def __str__(self):
        return "%s "% (self.user.nombre_usuario)+ "%s "% (self.user.paterno)+ "%s "% (self.user.materno)

class Docente_Guia(models.Model):
    id_guia = models.AutoField(primary_key = True)
    especialidad_docente = models.CharField(max_length = 220, blank = True, null = True)    
    user = models.OneToOneField(Usuario,on_delete=models.CASCADE,blank = True, null = True)
    guia = models.BooleanField(default = False)

    class Meta:
        verbose_name='Docente_Guia'
        verbose_name_plural='Docentes_Guias'

    def __str__(self):
        return "%s "% (self.user.nombre_usuario)+ "%s "% (self.user.paterno)+ "%s "% (self.user.materno)

class Docente_Revisor(models.Model):
    id_revisor = models.AutoField(primary_key = True)
    especialidad_docente = models.CharField(max_length = 220, blank = True, null = True)    
    user = models.OneToOneField(Usuario,on_delete=models.CASCADE,blank = True, null = True)
    revisor = models.BooleanField(default = False)
    class Meta:
        verbose_name='Docente_Revisor'
        verbose_name_plural='Docentes_Revisores'

    def __str__(self):
        return "%s "% (self.user.nombre_usuario)+ "%s "% (self.user.paterno)+ "%s "% (self.user.materno)
       
class Maestrante(models.Model):
    id_maestrante = models.AutoField(primary_key = True)
    
    especialidad_maestrante = models.CharField(max_length = 220, blank = True, null = True)    
    user = models.OneToOneField(Usuario,on_delete=models.CASCADE,blank = True, null = True)
    descripcion = models.CharField(max_length = 220, blank = True, null = True)    
    archivo_borrador = models.FileField(upload_to='tesis/actividades/borrador/', max_length=254,blank = True, null = True)     
    archivo_documento = models.FileField(upload_to='tesis/actividades/', max_length=254,blank = True, null = True)     
    avance_tesis = models.IntegerField( blank = False, null = True)
    tribunal = models.ForeignKey(Docente, on_delete=models.CASCADE,blank = True, null = True)
    guia = models.ForeignKey(Docente_Guia, on_delete=models.CASCADE,blank = True, null = True)
    revisor = models.ForeignKey(Docente_Revisor, on_delete=models.CASCADE,blank = True, null = True)
    tema_tesis = models.CharField('Tema de Tesis',max_length=200,blank=True,null=True)
    fecha_sustentacion = models.DateField(null=True, blank=True)
    hora_sustentacion = models.TimeField(null=True, blank=True)
    procedencia_tema = models.BooleanField(null=True, blank=True)
    fecha_formulario  = models.DateField('Fecha de entrega de formulario de habilitación',blank = False, null = True)    
    fecha_perfil  = models.DateField('Fecha de entrega de perfil de Tesis',blank = False, null = True)
    fecha_sustentacion  = models.DateField('Acto de sustentación de tema de Tesis',blank = False, null = True)
    fecha_desarrollo  = models.DateField('Desarrollo de la investigación',blank = False, null = True)

    #hora_sustentacion = models.TimeField(null=True, blank=True)
    class Meta:
        verbose_name='Maestrante'
        verbose_name_plural='Maestrantes'

    def __str__(self):
        return "%s "% (self.user.nombre_usuario)+ "%s "% (self.user.paterno)+ "%s "% (self.user.materno)



            	

class TecnicoPostgrado(models.Model):
    id_tecnico = models.AutoField(primary_key = True)    
    user = models.OneToOneField(Usuario,on_delete=models.CASCADE,blank = True, null = True)
    
    class Meta:
        verbose_name='Tecnico'
        verbose_name_plural='Tecnicos'

    def __str__(self):
       return "%s "% (self.user.nombre_usuario)+ "%s "% (self.user.paterno)+ "%s "% (self.user.materno)

class CoordinacionInvestigacion(models.Model):
    id_coordinacion_investigacion = models.AutoField(primary_key = True)    
    user = models.OneToOneField(Usuario,on_delete=models.CASCADE,blank = True, null = True)
    
    class Meta:
        verbose_name='Coordinacion Investigacion'
        verbose_name_plural='Coordinaciones Investigacion'

    def __str__(self):
       return "%s "% (self.user.nombre_usuario)+ "%s "% (self.user.paterno)+ "%s "% (self.user.materno)
    
class CoordinacionPostgrado(models.Model):
    id_coordinacion_postgrado = models.AutoField(primary_key = True)    
    user = models.OneToOneField(Usuario,on_delete=models.CASCADE,blank = True, null = True)
    
    class Meta:
        verbose_name='Coordinacion Postgrado'
        verbose_name_plural='Coordinaciones Postgrado'

    def __str__(self):
       return "%s "% (self.user.nombre_usuario)+ "%s "% (self.user.paterno)+ "%s "% (self.user.materno)





class ActividadesMaestrante(models.Model):
    id_actividad = models.AutoField(primary_key = True)    
    idmaestrante = models.IntegerField( blank = False, null = True)
    descripcion = models.CharField(max_length = 220, blank = True, null = True)    
    archivo_documento = models.FileField(upload_to='tesis/actividades/', max_length=254,blank = True, null = True)     
    fecha_publicacion = models.DateField('Fecha de publicación', auto_now = True, auto_now_add = False)       

    
    class Meta:
        verbose_name='Actividad'
        verbose_name_plural='Actividades'

    def __str__(self):

        return "%s "% (self.idmaestrante) 

 
class CentroActividades(models.Model):
    id_actividad = models.AutoField(primary_key = True)  
    idmaestrante = models.IntegerField( blank = False, null = True)
    usuario = models.CharField(max_length = 220, blank = True, null = True)
    actividad = models.CharField(max_length = 220, blank = True, null = True)
    fecha = models.CharField(max_length = 220, blank = True, null = True)
    class Meta:
        verbose_name='Centro_actividad'
        verbose_name_plural='Centro_actividades'

    def __str__(self):

        return "%s "% (self.fecha) 

class Cronograma(models.Model):
    id_cronograma = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length = 220, blank = True, null = True)
    fecha_asignado  = models.DateField('Fecha de asignación',blank = False, null = True)       
    fecha_entregado  = models.DateField('Fecha de entrega',blank = False, null = True)
    idmaestrante = models.IntegerField( blank = False, null = True)
    class Meta:
        verbose_name='Cronograma'
        verbose_name_plural='Cronogramas'

    def __str__(self):

        return "%s "% (self.descripcion)        




def crear_rol(sender,instance,created,**kwargs):
    if created:

        if instance.tipo_usuario==1:
            Maestrante.objects.create(user=instance,avance_tesis=1)
            
        if instance.tipo_usuario==2:
            Docente.objects.create(user=instance)
            Docente_Guia.objects.create(user=instance)
            Docente_Revisor.objects.create(user=instance)
        if instance.tipo_usuario==3:
            TecnicoPostgrado.objects.create(user=instance)
        if instance.tipo_usuario==4:
            CoordinacionInvestigacion.objects.create(user=instance)
        if instance.tipo_usuario==5:
            CoordinacionPostgrado.objects.create(user=instance)

post_save.connect(crear_rol,sender=Usuario)  


