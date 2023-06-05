from django.urls import path, re_path
from home import views

app_name = "home"

urlpatterns = [

    # The home page
    path('', views.home, name='home'),
#    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    
]