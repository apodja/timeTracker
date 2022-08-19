from django.urls import path
from .views import CheckAuthenticatedView, loginUser


urlpatterns = [
    path('login-check/', CheckAuthenticatedView.as_view()),
    path('login/', loginUser , name="login"),
]
