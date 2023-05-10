from django.urls import path, re_path
from . import views
urlpatterns=[
  
    path('fetch/', views.load_data,name='load_data'),
    path('listado_usuario/',views.ListadoUsuario.as_view(),name='listar_usuario'),
    path('listado_docente/',views.ListadoDocente.as_view(),name='listar_docente'),
    path('listado_maestrante/',views.ListadoMaestrante.as_view(),name='listar_maestrante'),
    path('listado_tecnico/',views.ListadoTecnico.as_view(),name='listar_tecnico'),
    path('listado_investigacion/',views.ListadoInvestigacion.as_view(),name='listar_investigacion'),
    path('listado_postgrado/',views.ListadoPostgrado.as_view(),name='listar_postgrado'),
    path('listado_tribunal/',views.ListadoTribunal.as_view(),name='listar_tribunal'),
    path('listado_guia/',views.ListadoGuia.as_view(),name='listar_guia'),
    path('listado_revisor/',views.ListadoRevisor.as_view(),name='listar_revisor'),
    

  

    path('registrar_usuario/',views.RegistrarUsuario.as_view(),name='registrar_usuario'),
    path('registrar_docente/',views.RegistrarDocente.as_view(),name='registrar_docente'),
    path('registrar_maestrante/',views.RegistrarMaestrante.as_view(),name='registrar_maestrante'),    
    path('registrar_tecnico/',views.RegistrarTecnico.as_view(),name='registrar_tecnico'),
    path('registrar_investigacion/',views.RegistrarInvestigacion.as_view(),name='registrar_investigacion'),
    path('registrar_postgrado/',views.RegistrarPostgrado.as_view(),name='registrar_postgrado'),
   
    path('editar_docente/<int:pk>',views.ActualizarDocente.as_view(), name = 'editar_docente'),
    path('editar_usuario/<int:pk>',views.ActualizarUsuario.as_view(), name = 'editar_usuario'),    
    path('editar_maestrante/<int:pk>',views.ActualizarMaestrante.as_view(), name = 'editar_maestrante'),
    path('editar_tecnico/<int:pk>',views.ActualizarTecnico.as_view(), name = 'editar_tecnico'),
    path('editar_investigacion/<int:pk>',views.ActualizarInvestigacion.as_view(), name = 'editar_investigacion'),
    path('editar_postgrado/<int:pk>',views.ActualizarPostgrado.as_view(), name = 'editar_postgrado'),
    path('editar_cronograma/<int:pk>',views.ActualizarCronograma.as_view(), name = 'editar_cronograma'),
    
    
    path('habilitarmaestranteguia/<int:pk>',views.HabilitarMaestranteGuia.as_view(), name = 'habilitarmaestranteguia'),
    path('habilitarmaestrantetribunal/<int:pk>',views.HabilitarMaestranteTribunal.as_view(), name = 'habilitarmaestrantetribunal'),
    path('habilitar_guia_revisor/<int:pk>',views.HabilitarGuiaRevisor.as_view(), name = 'habilitar_guia_revisor'),
   
    path('actividades',views.Actividades_Maestrante.as_view(),name='actividades'),
    path('act1',views.Actividad1.as_view(),name='act1'),
    path('act2',views.Actividad2.as_view(),name='act2'),
    path('act3',views.Actividad3.as_view(),name='act3'),
    path('act4',views.Actividad4.as_view(),name='act4'),
    path('act5',views.Actividad5.as_view(),name='act5'),
    path('act6',views.Actividad6.as_view(),name='act6'),
    path('act7',views.Actividad7.as_view(),name='act7'),
    path('act8',views.Actividad8.as_view(),name='act8'),
    path('act11',views.Actividad11.as_view(),name='act11'),

    path('cronograma',views.Cronograma.as_view(),name='cronograma'),

    path('fechasustentacion/<int:pk>',views.FechaSustentacion.as_view(),name='fechasustentacion'),

    path('activarguia/<int:pk>',views.Activar_Guia, name = 'activarguia'),
    path('activarrevisor/<int:pk>',views.Activar_Revisor, name = 'activarrevisor'),
    path('centro_actividad1/<int:pk>',views.Centro_actividad1, name = 'centro_actividad1'),
    
    path('procedenciatema/<int:pk>',views.ProcedenteTema, name = 'procedenciatema'),
    path('improcedenciatema/<int:pk>',views.ImProcedenteTema, name = 'improcedenciatema'),

    re_path('checklista1/$',views.check_lista1, name = 'checklista1'),
    re_path('checklista2/$',views.check_lista2, name = 'checklista2'),
    re_path('checklista3/$',views.check_lista3, name = 'checklista3'),
    re_path('checklista4/$',views.check_lista4, name = 'checklista4'),
    re_path('checklista5/$',views.check_lista5, name = 'checklista5'),
    re_path('checklista6/$',views.check_lista6, name = 'checklista6'),
    re_path('checklista7/$',views.check_lista7, name = 'checklista7'),
    re_path('checklista8/$',views.check_lista8, name = 'checklista8'),

    path('eliminar_usuario/<int:pk>',views.EliminarUsuario.as_view(), name = 'eliminar_usuario'),
    path('eliminar_docente/<int:pk>',views.EliminarDocente.as_view(), name = 'eliminar_docente'),
    path('eliminar_maestrante/<int:pk>',views.EliminarMaestrante.as_view(), name = 'eliminar_maestrante'),    
    path('eliminar_tecnico/<int:pk>',views.EliminarTecnico.as_view(), name = 'eliminar_tecnico'),
    path('eliminar_inestigacion/<int:pk>',views.EliminarInvestigacion.as_view(), name = 'eliminar_investigacion'),
    path('eliminar_postgrado/<int:pk>',views.EliminarPostgrado.as_view(), name = 'eliminar_postgrado')
]
