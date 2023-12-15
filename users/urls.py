from django.urls import path
from .views import user_registration, user_login

urlpatterns = [
    path('api/register/', user_registration, name='user-registration'),
    path('api/login/', user_login, name='user-login'),
]
