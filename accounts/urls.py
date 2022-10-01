from django.urls import path
from accounts.views import loginView, logoutView, register

urlpatterns = [
    path('login', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('register/', register, name='register')
    ]