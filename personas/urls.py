from django.urls import path
from .views import get_all#, crear, cancelar, nuevo, borrar
from personas import views

app_name = "personas"

urlpatterns = [
    path('', views.get_all, name='get_all'),
    path('get/<int:pk>', views.get_person, name='get'),
    path('add/', views.add_person, name='add'),
    path('delete/<str:pk>/', views.delete_person, name='delete'),
    path('edit/<str:pk>/', views.edit_person, name='edit'),
]