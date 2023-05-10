from django import forms
from django.contrib.auth.forms import AuthenticationForm
#from apps.usuario.models import Usuario
from .models import Usuario,Maestrante,Docente
from datetime import datetime
    
class FormularioEditar(forms.ModelForm):
    ci_usuario = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}),required=True,min_value=1, max_value=1000000000)
    ci_usuario = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}),required=True,min_value=1, max_value=1000000000)
    
    nombre_usuario = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120)
    paterno = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120)
    materno = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120)
    correo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","value":"@gmail.com"}),min_length=10, max_length=240)
    cel_usuario= forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}),required=True,min_value=1, max_value=1000000000)
    cel_usuario2= forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}),required=True,min_value=1, max_value=1000000000)
    descripcion= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120,required=False) 
    class Meta:
        model=Usuario
        fields=('ci_usuario','departamento','nombre_usuario','paterno','materno','cel_usuario','cel_usuario2','descripcion','correo')

class FormularioEditarMaestrante(forms.ModelForm):
    ci_usuario = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}),required=True,min_value=1, max_value=1000000000)
    
    nombre_usuario = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120)
    paterno = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120)
    materno = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120)
    correo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","value":"@gmail.com"}),min_length=10, max_length=240)
    cel_usuario= forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}),required=True,min_value=1, max_value=1000000000)
    cel_usuario2= forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}),required=True,min_value=1, max_value=1000000000)
    #descripcion= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120,required=False) 
    class Meta:
        model=Usuario
        fields=('ci_usuario','departamento','nombre_usuario','paterno','materno','cel_usuario','cel_usuario2','correo')
             

class FormularioUsuario(FormularioEditar):
 
    username= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120)
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese su contraseña',
            'id':'password1',
            'required':'required',
        }
    ))


    password2 = forms.CharField(label = 'Contraseña de confirmación',widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required',
        }
    ))
    
    class Meta:
        model=Usuario
        fields=('ci_usuario','departamento','nombre_usuario','paterno','materno','cel_usuario','descripcion','usuario_administrador','superusuario_administrador','tipo_usuario','username')
       
    def clean_pasaword2(self):
        """ validación de contraseñas
        Metodo que valida ambas contraseñas ingresadas sean igual
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class FormularioDocente(FormularioEditar):
    tipo_usuario = forms.IntegerField(widget=forms.NumberInput(attrs={"value":"2","type":"hidden"}),required=True)
    
    username= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120)
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese su contraseña',
            'id':'password1',
            'required':'required',
        }
    ))


    password2 = forms.CharField(label = 'Contraseña de confirmación',widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required',
        }
    ))
    
    class Meta:
        model=Usuario
        fields=('ci_usuario','departamento','nombre_usuario','paterno','materno','cel_usuario','cel_usuario2','descripcion','correo','tipo_usuario','username')
       
    def clean_pasaword2(self):
        """ validación de contraseñas
        Metodo que valida ambas contraseñas ingresadas sean igual
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user






class FormularioMaestrante(FormularioEditarMaestrante):
    tipo_usuario = forms.IntegerField(widget=forms.NumberInput(attrs={"value":"1","type":"hidden"}),required=True)
    
    username= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120)
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese su contraseña',
            'id':'password1',
            'required':'required',
        }
    ))


    password2 = forms.CharField(label = 'Contraseña de confirmación',widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required',
        }
    ))
    
    class Meta:
        model=Usuario
        fields=('ci_usuario','departamento','nombre_usuario','paterno','materno','cel_usuario','cel_usuario2','correo','tipo_usuario','username')
       
    def clean_pasaword2(self):
        """ validación de contraseñas
        Metodo que valida ambas contraseñas ingresadas sean igual
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class FormularioTecnico(FormularioEditar):
    tipo_usuario = forms.IntegerField(widget=forms.NumberInput(attrs={"value":"3","type":"hidden"}),required=True)
    
    username= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120)
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese su contraseña',
            'id':'password1',
            'required':'required',
        }
    ))


    password2 = forms.CharField(label = 'Contraseña de confirmación',widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required',
        }
    ))
    
    class Meta:
        model=Usuario
        fields=('ci_usuario','departamento','nombre_usuario','paterno','materno','cel_usuario','cel_usuario2','descripcion','correo','tipo_usuario','username')
       
    def clean_pasaword2(self):
        """ validación de contraseñas
        Metodo que valida ambas contraseñas ingresadas sean igual
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class FormularioInvestigacion(FormularioEditar):
    tipo_usuario = forms.IntegerField(widget=forms.NumberInput(attrs={"value":"4","type":"hidden"}),required=True)
    
    username= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120)
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese su contraseña',
            'id':'password1',
            'required':'required',
        }
    ))


    password2 = forms.CharField(label = 'Contraseña de confirmación',widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required',
        }
    ))
    
    class Meta:
        model=Usuario
        fields=('ci_usuario','departamento','nombre_usuario','paterno','materno','cel_usuario','cel_usuario2','descripcion','correo','tipo_usuario','username')
       
    def clean_pasaword2(self):
        """ validación de contraseñas
        Metodo que valida ambas contraseñas ingresadas sean igual
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class FormularioPostgrado(FormularioEditar):
    tipo_usuario = forms.IntegerField(widget=forms.NumberInput(attrs={"value":"5","type":"hidden"}),required=True)
    
    username= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=3, max_length=120)
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese su contraseña',
            'id':'password1',
            'required':'required',
        }
    ))


    password2 = forms.CharField(label = 'Contraseña de confirmación',widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required',
        }
    ))
    
    class Meta:
        model=Usuario
        fields=('ci_usuario','departamento','nombre_usuario','paterno','materno','cel_usuario','cel_usuario2','descripcion','correo','tipo_usuario','username')
       
    def clean_pasaword2(self):
        """ validación de contraseñas
        Metodo que valida ambas contraseñas ingresadas sean igual
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class FormularioHabilitarGuiaRevisor(forms.ModelForm):
    
    class Meta:
        model=Docente
        fields=('guia','revisor','tribunal')

class FormularioMaestranteGuia(forms.ModelForm):
 
    #tema_tesis = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=10, max_length=240)

    #maestrante = forms.ChoiceField(widget=forms.Select(attrs={"Disabled":"Disabled"}))
    class Meta:
        model=Maestrante
        fields=("guia",)
class FormularioMaestranteTribunal(forms.ModelForm):
 
    #tema_tesis = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),min_length=10, max_length=240)

    #maestrante = forms.ChoiceField(widget=forms.Select(attrs={"Disabled":"Disabled"}))
    class Meta:
        model=Maestrante
        fields=("tribunal",)

class FormularioFechaSustentacion(forms.ModelForm):
    class Meta:
        model = Maestrante
        fields = ('fecha_sustentacion','hora_sustentacion')
        widgets = {
            'fecha_sustentacion': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control',"required":"True"}
            ),
            'hora_sustentacion': forms.DateInput(
                attrs={'type': 'time', 'class': 'form-control',"required":"True"}
            )
                
        }
   

class FormularioCronograma(forms.ModelForm):
    class Meta:
        model = Maestrante
        fields = ('fecha_formulario','fecha_perfil','fecha_sustentacion','fecha_desarrollo')
        widgets = {
            'fecha_formulario': forms.DateInput(
                attrs={'type': 'date',  'class': 'form-control',"required":"True"}
            ),
            'fecha_perfil': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control',"required":"True"}
            ),
            'fecha_sustentacion': forms.DateInput(
                attrs={'type': 'date',  'class': 'form-control',"required":"True"}
            ),
            'fecha_desarrollo': forms.DateInput(
                attrs={'type': 'date',  'class': 'form-control',"required":"True"}
            )
        }


#        def __init__(self, *args, **kwargs):
#            super().__init__(*args, **kwargs)
#            self.fields['fecha_sustentacion'].widget.format = '%d/%m/%Y %H:%M'
#widgets = {
#            
#            'fecha_sustentacion': DateTimeInput(attrs={'class': 'form-control'}),
#            
#        }



