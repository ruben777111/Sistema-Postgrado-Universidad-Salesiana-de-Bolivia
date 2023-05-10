"""sispostgrado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path,include,re_path
from postgradoApp.views import index,exit

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('usuario/',include(('usuario.urls','usuario'))),
  
    path('video/', include(('video.urls','video'))),
    path('documento/', include(('documento.urls','documento'))),
    path('avance/', include(('avance.urls','avance'))),
    
    
    path('', index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('rooms/', include('room.urls')),
  
   
    ]

urlpatterns += [
    re_path(r'^tesis/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT,

    })
]