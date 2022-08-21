from django.urls import path
from .views import dashboard,timer
from .api import action,EntriesView


urlpatterns = [

    path('action/', action),
    path('entries/', EntriesView.as_view()),
    path('', dashboard, name='dashboard'),
    path('timer/', timer, name='timer')

]
