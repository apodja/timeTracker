from django.urls import path
from .views import index

urlpatterns = [
    path('projects/', index, name='projects' )
]
