from django.urls import path
from .views import CheckAuthenticatedView,LoginView


urlpatterns = [
    path('login-check/', CheckAuthenticatedView.as_view()),
    path('login/', LoginView.as_view()),
]
