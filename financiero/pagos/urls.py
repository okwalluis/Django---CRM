from django.contrib import admin
from django.urls import include, path
from financiero.pagos import views

app_name = "pagos"

urlpatterns = [
    path('pagar_cuota_por_id/<int:fk>/', views.pagar_cuota_por_id, name='pagar_cuota_por_id'),
]