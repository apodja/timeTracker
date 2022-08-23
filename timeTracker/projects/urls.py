from django.urls import path
from .views import index, project

urlpatterns = [
    path('projects/', index, name='projects' ),
    path('project/<int:pk>/', project, name='project' )
]
