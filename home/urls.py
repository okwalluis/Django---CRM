from django.urls import path, re_path
from home import views

app_name = "home"

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),    
]