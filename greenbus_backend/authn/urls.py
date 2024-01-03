from django.urls import path
from .views import get_all_users, user_signup, user_login

urlpatterns = [
    path('signup/', user_signup, name='user_signup'),
    path('login/', user_login, name='user_login'),
]
