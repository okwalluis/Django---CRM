from django.contrib import admin
from django.urls import include, path
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),             # UI Kits Html files
    #
    path('pagos/', include('pagos.urls')),
    path('personas/', include('personas.urls')),
    path('prestamos/', include('prestamos.urls')),
    
    path('users/', include(('users.urls', 'users'), namespace='users')),    
]
