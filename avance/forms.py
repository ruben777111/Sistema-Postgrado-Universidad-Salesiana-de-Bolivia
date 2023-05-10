from django import forms

#from apps.usuario.models import Usuario
from .models import Avance

    
class FormularioAvance(forms.ModelForm):  
    
    #maestrante = forms.IntegerField(widget=forms.HiddenInput())
    actividad = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120)
    
    obs = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    obs_ant = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120,required=False)
    
    class Meta:
        model=Avance
        fields=('maestrante','actividad','obs','obs_ant')


class FormularioAvanceVer(forms.ModelForm):  
    
    #maestrante = forms.IntegerField(widget=forms.HiddenInput())
    actividad = forms.CharField(widget=forms.TextInput(attrs={"readonly":"readonly","class":"form-control"}),min_length=3, max_length=120)
    
    obs = forms.CharField(widget=forms.Textarea(attrs={"readonly":"readonly",'rows': 5,"class":"form-control"}))
    obs_ant = forms.CharField(widget=forms.TextInput(attrs={"readonly":"readonly","class":"form-control"}),min_length=3, max_length=120,required=False)
    
    class Meta:
        model=Avance
        fields=('actividad','obs','obs_ant')