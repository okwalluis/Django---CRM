from django.urls import path
from base.personas import views

app_name = "personas"

urlpatterns = [
    path('', views.listar_personas, name='listar_personas'),
    path('listar_por_id/<int:pk>', views.listar_persona_por_id, name='listar_persona_por_id'),
    path('listar_por_string/<str:string>', views.listar_persona_string, name='listar_persona_string'),
    
    path('agregar/', views.agregar_persona, name='agregar_persona'),
    path('borrar/<str:pk>/', views.borrar_persona, name='borrar_persona'),
    path('editar/<str:pk>/', views.editar_persona, name='editar_persona'),
    ## direcciones
    path('borrar_direccion/<str:pk>/', views.borrar_direccion, name='borrar_direccion'),
    ## documentos
    path('borrar_documento/<str:pk>/', views.borrar_documento, name='borrar_documento'),
    ## telefonos
    path('borrar_telefono/<str:pk>/', views.borrar_telefono, name='borrar_telefono'),
]