from django.urls import path, re_path
from home import views

app_name = "home"

urlpatterns = [

    # The home page
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
#    path('login/', views.login_user, name='login'),
#    path('register/<int:pk>', views.persona_record, name='persona_record'),
#    path('delete/<int:pk>', views.delete_record, name='delete_record'),
#    path('add/', views.add_record, name='add_record'),
    
    
]