from django.urls import path
from personas import views

app_name = "personas"

urlpatterns = [
    path('', views.listar_personas, name='listar_personas'),
    path('listar_por_id/<int:pk>', views.listar_persona_por_id, name='listar_persona_por_id'),
    path('agregar/', views.agregar_persona, name='agregar_persona'),
    path('borrar/<str:pk>/', views.borrar_persona, name='borrar_persona'),
    path('editar/<str:pk>/', views.editar_persona, name='editar_persona'),
    ## 
    
]