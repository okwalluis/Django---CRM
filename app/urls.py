from django.contrib import admin
from django.urls import include, path
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.home.urls')),             # UI Kits Html files
    path('personas/', include('base.personas.urls')),
    path('users/', include(('base.users.urls', 'users'), namespace='users')),    
    #
    path('pagos/', include('financiero.pagos.urls')),
    path('prestamos/', include('financiero.prestamos.urls')),
    
]
