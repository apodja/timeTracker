from django.urls import path
from .views import index, project,add_task,delete_task

urlpatterns = [
    path('projects/', index, name='projects' ),
    path('project/<int:pk>/', project, name='project' ),
    path('project/add_task/', add_task, name='add_task' ),
    path('project/delete_task/<int:project_id>/<int:task_id>/', delete_task, name='delete_task' )
]
