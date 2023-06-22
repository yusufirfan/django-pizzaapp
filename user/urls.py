from django.urls import path
from .views import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
]