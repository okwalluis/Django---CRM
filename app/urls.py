from django.contrib import admin
from django.urls import include, path

#{% url 'posts:detail' post.url%}
    #path('', include(('posts.urls', 'posts'), namespace='posts')),
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),             # UI Kits Html files
    path('personas/', include('personas.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users')),    
]
