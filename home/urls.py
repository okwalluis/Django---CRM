from django.urls import path, re_path
from home import views

app_name = "home"

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
]