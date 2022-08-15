from django.urls import path
from .views import startTime, stopTime

urlpatterns = [
    path('start/', startTime),
    path('stop/', stopTime),
]
