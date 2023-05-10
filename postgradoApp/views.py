from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.contrib import messages
# Create your views here.


#vista basada en clases
@method_decorator(login_required, name='dispatch')
class Inicio(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')

#vista basada en funciones
@login_required
def index(request):
    return render(request,"index.html")


#Salir
def exit(request):
    logout(request)
    return redirect("index.html")

