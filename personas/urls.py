from django.urls import path
from .views import PersonaView, crear, cancelar, nuevo, borrar

app_name = "persona"

#{% url 'posts:detail' post.url%}
    #path('', include(('posts.urls', 'posts'), namespace='posts')),

urlpatterns = [
    path('', PersonaView.as_view(), name='personas'),
    path('nuevo/', nuevo, name='nuevo'),
    path('crear/', crear, name='crear'),
    path('cancelar/', cancelar, name='cancelar'),
    path('borrar/<str:pk>/', borrar, name='borrar'),
]

"""
urlpatterns = [
    path('', views.personas_list, name='personas-list'),
    path('create/', views.create_persona, name='crear-persona'),
    path('edit/<str:pk>/', views.edit_persona, name='editar-persona'),
    path('delete/<str:pk>/', views.delete_persona, name='borrar-persona'),
]

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

urlpatterns = [
    path(route='',view=views.PostsFeedView.as_view(),name='blog'),
    path(route='posts/<slug:url>/',view=views.PostDetailView.as_view(),name='detail'),
    path(route='posts/save_comment',view=views.save_comment,name='save_comment'),
]
"""