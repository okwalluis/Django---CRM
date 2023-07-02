from django.urls import path
from prestamos import views

app_name = "prestamos"

urlpatterns = [
    path('', views.listar_prestamos, name='listar_prestamos'),
    path('listar_prestamo_por_id/<int:pk>', views.listar_prestamo_por_id, name='listar_prestamo_por_id'),
    path('agregar/', views.agregar_prestamo, name='agregar_prestamo'),
    path('editar/<int:pk>/', views.editar_prestamo, name='editar_prestamo'),

    ### Crear urls para las clases secundarias fk ya que es con relacion al prestamo
    path('listar_cuotas_por_id/<int:fk>', views.listar_cuotas_por_id, name='listar_cuotas_por_id'),
    path('generar_pagare/<int:fk>', views.generar_pagare, name='generar_pagare'),    
]