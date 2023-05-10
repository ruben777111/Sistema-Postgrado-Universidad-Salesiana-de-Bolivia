from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from avance.models import Avance
from django.views.generic import View,UpdateView, CreateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import FormularioAvance,FormularioAvanceVer
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

@method_decorator(login_required, name='dispatch')
class ListadoAvance(View):
    
    model = Avance
    template_name = 'avance/listar_avance.html'
    context_object_name = 'avances'
    queryset = Avance.objects.filter(estado_avance = True)
    
    def get_queryset(self):
        return self.model.objects.filter(estado_avance=True)
    def get_context_data(self, **kwargs):
        contexto={}
        contexto['avances']=self.get_queryset()
        return contexto
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())

@method_decorator(login_required, name='dispatch')  
class RegistrarAvance(LoginRequiredMixin,CreateView):
    model=Avance
    
    form_class=FormularioAvance
    template_name='avance/agregar_avance.html'
    success_url = reverse_lazy('avance:listar_avance')
    def form_valid(self, form_class):
        self.object = form_class.save(commit=False)
        self.object.nombre_docente = self.request.user.nombre_usuario+" "+self.request.user.paterno+" "+self.request.user.materno
        self.object.docente = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())




@method_decorator(login_required, name='dispatch')
class ActualizarAvance(UpdateView):

    model = Avance
    template_name = 'avance/editar_avance.html'
    form_class = FormularioAvanceVer
    success_url = reverse_lazy('avance:listar_avance')    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['avance'] = Avance.objects.filter(estado_avance = True)
        return context

@method_decorator(login_required, name='dispatch')
class EliminarAvance(DeleteView):
    model = Avance

    def post(self,request,pk,*args,**kwargs):
        object = Avance.objects.get(id = pk)
        object.docente = True
        object.save()
        return redirect ('avance:listar_avance')
    
