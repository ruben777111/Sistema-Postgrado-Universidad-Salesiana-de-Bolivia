from django.urls import path
from . import views
urlpatterns = [
  
    path('listar_avance/',views.ListadoAvance.as_view(), name='listar_avance'),
    path('registrar_avance/',views.RegistrarAvance.as_view(),name='registrar_avance'),

    path('editar_avance/<int:pk>',views.ActualizarAvance.as_view(), name = 'editar_avance'),
    path('eliminar_avance/<int:pk>',views.EliminarAvance.as_view(), name = 'eliminar_avance')

    ]