from django.urls import path
from .views import action,EntriesView
from .adminAPI import EntriesViewAdmin

urlpatterns = [

    path('action/', action),
    path('entries/', EntriesView.as_view()),

    #admin urls
    path('admin/entries/', EntriesViewAdmin.as_view()),
]
