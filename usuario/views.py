#from .apps.usuario.models import Usuario

from django.shortcuts import render,redirect,get_object_or_404

from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.messages.views import SuccessMessageMixin

from .forms import FormularioCronograma,FormularioMaestranteTribunal,FormularioFechaSustentacion,FormularioUsuario,FormularioEditar,FormularioDocente,FormularioMaestrante,FormularioTecnico,FormularioInvestigacion,FormularioPostgrado,FormularioHabilitarGuiaRevisor,FormularioMaestranteGuia,FormularioEditarMaestrante
from usuario.models import CentroActividades,Docente_Guia,Docente_Revisor,Docente,ActividadesMaestrante,Usuario,Maestrante
from room.models import Room 
from django.views.generic import View,TemplateView,ListView,UpdateView, CreateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage


from django.shortcuts import render, get_object_or_404

from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from django.urls import reverse
from django.views.generic import View


# *************** Listas de usuarios *******************.
@method_decorator(login_required, name='dispatch')
class ListadoUsuario(SuccessMessageMixin,ListView):
    model=Usuario
    template_name='usuario/listar_usuario.html'
    success_message = " was created successfully"
    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=False)

@method_decorator(login_required, name='dispatch')
class ListadoMaestrante(ListView):
    model=Usuario
    template_name='usuario/listar_maestrante.html'

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True).filter(tipo_usuario=1).order_by('fecha_registro')

@method_decorator(login_required, name='dispatch')
class ListadoDocente(ListView):
    model=Docente
    template_name='usuario/listar_docente.html'

    def get_queryset(self):
        return self.model.objects.filter()
    
@method_decorator(login_required, name='dispatch')
class ListadoGuia(ListView):
    model=Docente_Guia
    template_name='usuario/listar_guia.html'

    def get_queryset(self):
        return self.model.objects.filter()
       
@method_decorator(login_required, name='dispatch')
class ListadoRevisor(ListView):
    model=Docente_Revisor   
    template_name='usuario/listar_revisor.html'

    def get_queryset(self):
        return self.model.objects.filter()

@method_decorator(login_required, name='dispatch')
class ListadoTribunal(ListView):
    model=Docente_Revisor   
    template_name='usuario/listar_revisor.html'

    def get_queryset(self):
        return self.model.objects.filter()
@method_decorator(login_required, name='dispatch')
class ListadoTecnico(ListView):
    model=Usuario
    template_name='usuario/listar_tecnico.html'

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True).filter(tipo_usuario=3)

@method_decorator(login_required, name='dispatch')
class ListadoInvestigacion(ListView):
    model=Usuario
    template_name='usuario/listar_investigacion.html'

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True).filter(tipo_usuario=4)

@method_decorator(login_required, name='dispatch')
class ListadoPostgrado(ListView):
    model=Usuario
    template_name='usuario/listar_postgrado.html'

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True).filter(tipo_usuario=5)




# *************** Registro de usuarios *******************.

@method_decorator(login_required, name='dispatch')
class RegistrarUsuario(CreateView):
    model=Usuario
    form_class=FormularioUsuario
    template_name='usuario/crear_usuario.html'
    success_url = reverse_lazy('usuario:listar_usuario')

@method_decorator(login_required, name='dispatch')
class RegistrarDocente(CreateView):
    model=Usuario
    form_class=FormularioDocente
    template_name='usuario/agregar_docente.html'
    success_url = reverse_lazy('usuario:listar_docente')

@method_decorator(login_required, name='dispatch')
class RegistrarMaestrante(CreateView):
    model=Usuario
    form_class=FormularioMaestrante
    template_name='usuario/agregar_maestrante.html'
    success_url = reverse_lazy('usuario:listar_maestrante')



@method_decorator(login_required, name='dispatch')
class RegistrarTecnico(CreateView):
    model=Usuario
    form_class=FormularioTecnico
    template_name='usuario/agregar_tecnico.html'
    success_url = reverse_lazy('usuario:listar_tecnico')

@method_decorator(login_required, name='dispatch')
class RegistrarInvestigacion(CreateView):
    model=Usuario
    form_class=FormularioInvestigacion
    template_name='usuario/agregar_investigacion.html'
    success_url = reverse_lazy('usuario:listar_investigacion')

@method_decorator(login_required, name='dispatch')
class RegistrarPostgrado(CreateView):
    model=Usuario
    form_class=FormularioPostgrado
    template_name='usuario/agregar_postgrado.html'
    success_url = reverse_lazy('usuario:listar_postgrado')


@method_decorator(login_required, name='dispatch')
class RegistrarPostgrado(CreateView):
    model=Usuario
    form_class=FormularioPostgrado
    template_name='usuario/agregar_postgrado.html'
    success_url = reverse_lazy('usuario:listar_postgrado')

# *************** Actualizar datos de usuarios *******************.

@method_decorator(login_required, name='dispatch')
class ActualizarPostgrado(UpdateView):

    model = Usuario
    template_name = 'usuario/editar_usuario.html'
    form_class = FormularioEditar
    success_url = reverse_lazy('usuario:listar_usuario')    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        
        context['usuario'] = Usuario.objects.filter(usuario_activo = True)
        return context
  
  
 
 
@method_decorator(login_required, name='dispatch')
class ActualizarInvestigacion(UpdateView):

    model = Usuario
    template_name = 'usuario/editar_usuario.html'
    form_class = FormularioEditar
    success_url = reverse_lazy('usuario:listar_usuario')    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = Usuario.objects.filter(usuario_activo = True)
        return context

@method_decorator(login_required, name='dispatch')
class ActualizarTecnico(UpdateView):

    model = Usuario
    template_name = 'usuario/editar_usuario.html'
    form_class = FormularioEditar
    success_url = reverse_lazy('usuario:listar_usuario')    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = Usuario.objects.filter(usuario_activo = True)
        return context

@method_decorator(login_required, name='dispatch')
class ActualizarMaestrante(SuccessMessageMixin,UpdateView):

    model = Usuario
    template_name = 'usuario/editar_usuario.html'
    form_class = FormularioEditarMaestrante
    success_url = reverse_lazy('usuario:act1') 
    success_message="guassrgado"   
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = Usuario.objects.filter(usuario_activo = True)
        return context

@method_decorator(login_required, name='dispatch')
class ActualizarDocente(UpdateView):

    model = Usuario
    template_name = 'usuario/editar_usuario.html'
    form_class = FormularioEditar
    success_url = reverse_lazy('usuario:listar_usuario')    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = Usuario.objects.filter(usuario_activo = True)
        return context

@method_decorator(login_required, name='dispatch')    
class ActualizarUsuario(SuccessMessageMixin,UpdateView):

    model = Usuario
    template_name = 'usuario/editar_usuario.html'
    form_class = FormularioEditar
    success_url = reverse_lazy('usuario:listar_usuario')
    success_message = "%(calculated_field)s was created successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.calculated_field,
        )
   
@method_decorator(login_required, name='dispatch')
class ActualizarCronograma(SuccessMessageMixin,UpdateView):

    model = Maestrante
    template_name = 'usuario/editar_cronograma.html'
    form_class = FormularioCronograma
    success_url = reverse_lazy('usuario:act2') 
 



@method_decorator(login_required, name='dispatch')    
class HabilitarGuiaRevisor(UpdateView):

    model = Docente
    template_name = 'usuario/habilitar_guia_revisor.html'
    form_class = FormularioHabilitarGuiaRevisor
    success_url = reverse_lazy('usuario:listar_docente')    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = Docente.objects.filter()
        return context

@method_decorator(login_required, name='dispatch')    
class HabilitarMaestranteGuia(UpdateView):

    model = Maestrante
    template_name = 'usuario/editar_maestrante_guia.html'
    form_class = FormularioMaestranteGuia
    success_url = reverse_lazy('usuario:act4')    

@method_decorator(login_required, name='dispatch')    
class HabilitarMaestranteTribunal(UpdateView):

    model = Maestrante
    template_name = 'usuario/editar_maestrante_tribunal.html'
    form_class = FormularioMaestranteTribunal
    success_url = reverse_lazy('usuario:act7')    





    
# *************** Eliminar datos de usuarios *******************.


@method_decorator(login_required, name='dispatch')
class EliminarUsuario(DeleteView):
    model = Usuario

    def post(self,request,pk,*args,**kwargs):
        object = Usuario.objects.get(id = pk)
        object.usuario_activo = False
        object.save()
        return redirect ('usuario:act1')

@method_decorator(login_required, name='dispatch')
class EliminarDocente(DeleteView):
    model = Usuario

    def post(self,request,pk,*args,**kwargs):
        object = Usuario.objects.get(id = pk)
        object.usuario_activo = False
        object.save()
        return redirect ('usuario:listar_docente')


@method_decorator(login_required, name='dispatch')
class EliminarMaestrante(DeleteView):
    model = Usuario

    def post(self,request,pk,*args,**kwargs):
        object = Usuario.objects.get(id = pk)
        object.usuario_activo = False
        object.save()
        return redirect ('usuario:act1')



@method_decorator(login_required, name='dispatch')
class EliminarTecnico(DeleteView):
    model = Usuario

    def post(self,request,pk,*args,**kwargs):
        object = Usuario.objects.get(id = pk)
        object.usuario_activo = False
        object.save()
        return redirect ('usuario:listar_tecnico')

@method_decorator(login_required, name='dispatch')    
class EliminarInvestigacion(DeleteView):
    model = Usuario

    def post(self,request,pk,*args,**kwargs):
        object = Usuario.objects.get(id = pk)
        object.usuario_activo = False
        object.save()
        return redirect ('usuario:listar_investigacion')

@method_decorator(login_required, name='dispatch')
class EliminarPostgrado(DeleteView):
    model = Usuario

    def post(self,request,pk,*args,**kwargs):
        object = Usuario.objects.get(id = pk)
        object.usuario_activo = False
        object.save()
        return redirect ('usuario:listar_postgrado')



@method_decorator(login_required, name='dispatch')
class Actividades_Maestrante(View):
    
    model=ActividadesMaestrante
    template_name='usuario/act/actividades.html'
    context_object_name = 'actividadess'
    queryset = ActividadesMaestrante.objects.filter()
    
    def get_queryset(self):
        return self.model.objects.filter()
 
    def get_context_data(self, **kwargs):
        contexto={}
        contexto['actividadess']=self.get_queryset()
        return contexto

    def get(self,request,**kwargs):
        if self.request.user.tipo_usuario == 1:
            return render(request,self.template_name,self.get_context_data())
            
        return HttpResponseForbidden('Error')
# *************** 1 Inducción y asesoramiento para el proceso de tesis  *******************.
# *************** Información al postulante sobre el proceso de Tesis  *******************.


@method_decorator(login_required, name='dispatch')
class Actividad1(View):
    
    model=Maestrante
    template_name='usuario/act/act1.html'
    context_object_name = 'actividades'
    queryset = Maestrante.objects.filter(avance_tesis=1)
    
    def get_queryset(self):
        return self.model.objects.filter(avance_tesis=1)
 
    def get_context_data(self, **kwargs):
        contexto={}
        contexto['actividades']=self.get_queryset()
        return contexto

    def get(self,request,**kwargs):
        if self.request.user.tipo_usuario == 3 or self.request.user.tipo_usuario == None:
            return render(request,self.template_name,self.get_context_data())
            
        return HttpResponseForbidden('Error')

@method_decorator(login_required, name='dispatch')
class Actividad2(View):
    
    model=Maestrante
    template_name='usuario/act/act2.html'
    context_object_name = 'actividades'
    queryset = Maestrante.objects.filter(avance_tesis=2)
    
    def get_queryset(self):
        return self.model.objects.filter(avance_tesis=2)
 
    def get_context_data(self, **kwargs):
        contexto={}
        contexto['actividades']=self.get_queryset()
        return contexto

    def get(self,request,**kwargs):
        if self.request.user.tipo_usuario == 3 or self.request.user.tipo_usuario == 4:
            return render(request,self.template_name,self.get_context_data())
            
        return HttpResponseForbidden('Error')

         
@method_decorator(login_required, name='dispatch')
class Actividad3(View):
    
    model=Maestrante
    template_name='usuario/act/act3.html'
    context_object_name = 'actividades'
    queryset = Maestrante.objects.filter(avance_tesis=3)
    
    def get_queryset(self):
        return self.model.objects.filter(avance_tesis=3)
 
    def get_context_data(self, **kwargs):
        contexto={}
        contexto['actividades']=self.get_queryset()
        return contexto

    def get(self,request,**kwargs):
        if self.request.user.tipo_usuario == 3 or self.request.user.tipo_usuario == 4:
            return render(request,self.template_name,self.get_context_data())
            
        return HttpResponseForbidden('Error')



# *************** Acompañamiento al postulante en la elaboración de su Perfil de Tesis o actualización de su documento de Tesis *******************.
@method_decorator(login_required, name='dispatch')
class Actividad4(View):
    
    model=Maestrante
    template_name='usuario/act/act4.html'
    context_object_name = 'actividades'
    queryset = Maestrante.objects.filter(avance_tesis=4)
   
    
    def get_queryset(self):
        return self.model.objects.filter(avance_tesis=4)
 
    def get_context_data(self, **kwargs):
        contexto={}
        contexto['actividades']=self.get_queryset()
        return contexto

    def get(self,request,**kwargs):
        if self.request.user.tipo_usuario == 2 or self.request.user.tipo_usuario == 3 :
            return render(request,self.template_name,self.get_context_data())
            
        return HttpResponseForbidden('Error')

@method_decorator(login_required, name='dispatch')
class Actividad5(View):
    
    model=Maestrante
    template_name='usuario/act/act5.html'
    context_object_name = 'actividades'
    queryset = Maestrante.objects.filter(avance_tesis=5)
    
    def get_queryset(self):
        return self.model.objects.filter(avance_tesis=5)
 
    def get_context_data(self, **kwargs):
        contexto={}
        contexto['actividades']=self.get_queryset()
        return contexto

    def get(self,request,**kwargs):
        if self.request.user.tipo_usuario == 2 or self.request.user.tipo_usuario == 3 :
            return render(request,self.template_name,self.get_context_data())
            
        return HttpResponseForbidden('Error')

@method_decorator(login_required, name='dispatch')
class Actividad6(View):
    
    model=Maestrante
    template_name='usuario/act/act6.html'
    context_object_name = 'actividades'
    queryset = Maestrante.objects.filter(avance_tesis=6)
    
    def get_queryset(self):
        return self.model.objects.filter(avance_tesis=6)
 
    def get_context_data(self, **kwargs):
        contexto={}
        contexto['actividades']=self.get_queryset()
        return contexto

    def get(self,request,**kwargs):
        if  self.request.user.tipo_usuario == 3 :
            return render(request,self.template_name,self.get_context_data())
            
        return HttpResponseForbidden('Error')

@method_decorator(login_required, name='dispatch')
class Actividad7(View):
    
    model=Maestrante
    template_name='usuario/act/act7.html'
    context_object_name = 'actividades'
    queryset = Maestrante.objects.filter(avance_tesis=7)
    
    def get_queryset(self):
        return self.model.objects.filter(avance_tesis=7)
 
    def get_context_data(self, **kwargs):
        contexto={}
        contexto['actividades']=self.get_queryset()
        return contexto

    def get(self,request,**kwargs):
        if  self.request.user.tipo_usuario == 5 :
            return render(request,self.template_name,self.get_context_data())
            
        return HttpResponseForbidden('Error')
    
@method_decorator(login_required, name='dispatch')
class Actividad8(View):
    
    model=Maestrante
    template_name='usuario/act/act8.html'
    context_object_name = 'actividades'
    queryset = Maestrante.objects.filter(avance_tesis=8)
    
    def get_queryset(self):
        return self.model.objects.filter(avance_tesis=8)
 
    def get_context_data(self, **kwargs):
        contexto={}
        contexto['actividades']=self.get_queryset()
        return contexto

    def get(self,request,**kwargs):
        if  self.request.user.tipo_usuario == 2 or self.request.user.tipo_usuario == 3:
            return render(request,self.template_name,self.get_context_data())
            
        return HttpResponseForbidden('Error')


@method_decorator(login_required, name='dispatch')
class Actividad11(View):
    
    model=Maestrante
    template_name='usuario/act/act11.html'
    context_object_name = 'actividades'
    queryset = Maestrante.objects.filter(avance_tesis=11)
    
    def get_queryset(self):
        return self.model.objects.filter(avance_tesis=11)
 
    def get_context_data(self, **kwargs):
        contexto={}
        contexto['actividades']=self.get_queryset()
        return contexto

    def get(self,request,**kwargs):
        if  self.request.user.tipo_usuario == 3 or self.request.user.tipo_usuario == 5:
            return render(request,self.template_name,self.get_context_data())
            
        return HttpResponseForbidden('Error')
@method_decorator(login_required, name='dispatch')    
class FechaSustentacion(UpdateView):

    model = Maestrante
    template_name = 'usuario/act/fechasustentacion.html'
    form_class = FormularioFechaSustentacion
    success_url = reverse_lazy('usuario:act7')    
    
@method_decorator(login_required, name='dispatch')
class Cronograma(View):
    
    model=Maestrante
    template_name='usuario/act/cronograma.html'
    context_object_name = 'actividades'
    queryset = Maestrante.objects.filter()
    
    def get_queryset(self):
        return self.model.objects.filter()
 
    def get_context_data(self, **kwargs):
        contexto={}
        contexto['actividades']=self.get_queryset()
        return contexto

    def get(self,request,**kwargs):
        if  self.request.user.tipo_usuario == 1 or self.request.user.tipo_usuario == 3:
            return render(request,self.template_name,self.get_context_data())
            
        return HttpResponseForbidden('Error')
    
# *************** 2 Sustentación del tema de investigación de Tesis *******************.

def ProcedenteTema(request,pk):
    activar = get_object_or_404(Maestrante,id_maestrante=pk)
    activar.procedencia_tema=True
    activar.save()
    
    return redirect('usuario:act8')
def ImProcedenteTema(request,pk):
    activar = get_object_or_404(Maestrante,id_maestrante=pk)
    activar.procedencia_tema=False
    activar.save()
    
    return redirect('usuario:act8')
def Activar_Guia(request,pk):
    activar = get_object_or_404(Docente_Guia,id_guia=pk)
    if activar.guia:
        activar.guia=False
    else:
        activar.guia=True
    activar.save()
    
    return redirect('usuario:listar_guia')

def Activar_Revisor(request,pk):
    activar = get_object_or_404(Docente_Revisor,id_revisor=pk)
    if activar.revisor:
        activar.revisor=False
    else:
        activar.revisor=True
    activar.save()
    
    return redirect('usuario:listar_revisor')

def Centro_actividad1(request,pk):
    paso = get_object_or_404(Maestrante,id_maestrante=pk)
    paso.avance_tesis=2
    paso.save()
    
    return redirect('usuario:act1')


def check_lista1(request):
    
    if request.method =='POST':
        actividad = "Actividad 1 de alta"
        fecha = request.POST['fecha']
        usuario = request.POST['usuario']
        check = request.POST.getlist('checks[]')
     
        for i in check:
            CentroActividades.objects.create(idmaestrante=i,usuario=usuario,actividad=actividad,fecha=fecha)
       
            b = Maestrante.objects.get(pk=i)
            b.avance_tesis=2
            b.save()
    return redirect('usuario:act1')
    
      
def check_lista2(request):
    
    if request.method =='POST':
        check = request.POST.getlist('checks[]')
        actividad = "Actividad 2 de alta"
        fecha = request.POST['fecha']
        usuario = request.POST['usuario']
        for i in check:
            CentroActividades.objects.create(idmaestrante=i,usuario=usuario,actividad=actividad,fecha=fecha)
            b = Maestrante.objects.get(pk=i)
            b.avance_tesis=2
            b.save()
            b = Maestrante.objects.get(pk=i)
            b.avance_tesis=3
            b.save()
    return redirect('usuario:act2')   



def check_lista3(request):


    if request.method =='POST':
        actividad = "Actividad 3 de alta"
        fecha = request.POST['fecha']
        usuario = request.POST['usuario']
        descripcion = request.POST['descripcion']
        documento = request.FILES['documento']  
        check = request.POST.getlist('checks[]')
     
        for i in check:
            b = Maestrante.objects.get(pk=i)
            b.avance_tesis=4
            b.save()
            CentroActividades.objects.create(idmaestrante=i,usuario=usuario,actividad=actividad,fecha=fecha)
            ActividadesMaestrante.objects.create(idmaestrante=i,descripcion=descripcion,archivo_documento=documento)
              

    return redirect('usuario:act3')      




def check_lista4(request):
    
    if request.method =='POST':
        actividad = "Actividad 4 de alta"
        fecha = request.POST['fecha']
        usuario = request.POST['usuario']

      

        check = request.POST.getlist('checks[]')
        
        if check:
            for i in check:  
                CentroActividades.objects.create(idmaestrante=i,usuario=usuario,actividad=actividad,fecha=fecha)           
                
                
                b = Maestrante.objects.get(pk=i)
                b.avance_tesis=5                
                Room.objects.create(idmaestrante=b.id_maestrante,iddocente=b.guia.id_guia,name=b.guia.user.nombre_usuario+" "+b.guia.user.paterno+" "+b.guia.user.materno+" - "+b.user.nombre_usuario+" "+b.user.paterno+" "+b.user.materno,slug=b.user)
                b.save()

    
    return redirect('usuario:act4') 


def check_lista5(request):
    
    if request.method =='POST':
        actividad = "Actividad 5 de alta"
        fecha = request.POST['fecha']
        usuario = request.POST['usuario']
        check = request.POST.getlist('checks[]')
        
        if check:
            for i in check:  
                           
                
                CentroActividades.objects.create(idmaestrante=i,usuario=usuario,actividad=actividad,fecha=fecha)           
                b = Maestrante.objects.get(pk=i)
                b.avance_tesis=6
                b.save()
    
    return redirect('usuario:act5')  

def check_lista6(request):
    
    if request.method =='POST':
        actividad = "Actividad 6 de alta"
        fecha = request.POST['fecha']
        usuario = request.POST['usuario']
        check = request.POST.getlist('checks[]')
        
        if check:
            for i in check:  
                CentroActividades.objects.create(idmaestrante=i,usuario=usuario,actividad=actividad,fecha=fecha)           
                b = Maestrante.objects.get(pk=i)
                b.avance_tesis=7
                b.save()
    
    return redirect('usuario:act6') 

def check_lista7(request):
    
    if request.method =='POST':
        actividad = "Actividad 7 de alta"
        fecha = request.POST['fecha']
        usuario = request.POST['usuario']
        descripcion = request.POST['descripcion']
        check = request.POST.getlist('checks[]')
        
        if check:
            for i in check: 
                CentroActividades.objects.create(idmaestrante=i,usuario=usuario,actividad=actividad,fecha=fecha)           
                b = Maestrante.objects.get(pk=i)                
                b.avance_tesis=8
                b.save()
              
             
                ActividadesMaestrante.objects.create(idmaestrante=i,descripcion=descripcion+" fecha : "+str(b.fecha_sustentacion)+" Hrs. "+str(b.hora_sustentacion))
    
    return redirect('usuario:act7') 


def check_lista8(request):
    
    if request.method =='POST':
        actividad = "Actividad 8 de alta"
        fecha = request.POST['fecha']
        usuario = request.POST['usuario']
        descripcion = request.POST['descripcion']
        check = request.POST.getlist('checks[]')
        
        if check:
            for i in check:                 
                b = Maestrante.objects.get(pk=i)
                if b.procedencia_tema:
                    descripcion=descripcion+" ha sido procedente"
                    b.avance_tesis=11
                    b.save()
                else:
                    descripcion=descripcion+" no ha sido procedente, favor de comunicarse con Postgrado" 
                CentroActividades.objects.create(idmaestrante=i,usuario=usuario,actividad=actividad,fecha=fecha)           
                ActividadesMaestrante.objects.create(idmaestrante=i,descripcion=descripcion)
               
    return redirect('usuario:act8') 


#proceso pendiente
#comunicados
#actividades
def load_data(request):
    object_list = Maestrante.objects.all()
    json = serializers.serialize('json', object_list)
    return HttpResponse(json, content_type='application/json')
class PostStore(View):
    form_class = FormularioEditarMaestrante
    template_name = 'json.html'

    def post(self, request):
        form = self.form_class(request.POST)
        data = {'error': form.errors}
        if form.is_valid():
            try:
                title = request.POST.get('guia')
                description = request.POST.get('description')

                obj = get_object_or_404(Maestrante, id=request.POST.get('post_id'))
                obj.title=title
                obj.description=description
                obj.save()
                return JsonResponse({'success': True, 'message': 'Post Updated Successfully!'})
            except:
                obj = Maestrante(guia=request.POST.get('guia')) #add more fields
                obj.save()
                return JsonResponse({'success': True, 'message': 'Post Created Successfully!'})
        else:
            return JsonResponse({'error': True, 'error': form.errors})
        return render(request, self.template_name,{'data':data})

def post_edit(request,id):
    if request.method == 'GET':

        posts = Maestrante.objects.filter(id=id).first()

        return JsonResponse({'id':posts.id,'title':posts.title,'description':posts.description})
    else:
        return JsonResponse({'errors':'Something went wrong!'})

def post_delete(request,id):
    post = Maestrante.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))