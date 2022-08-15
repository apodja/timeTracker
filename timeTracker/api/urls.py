from django.urls import path
from .views import action,EntriesView

urlpatterns = [

    path('action/', action),
    path('entries/', EntriesView.as_view())
]
