from django.urls import path
from .views import login_page, login_user, logout_user

urlpatterns = [
  path('login/', login_page, name='login'),
  path('login-user/', login_user, name='login_user'),
  path('logout/', logout_user, name='logout'),
]