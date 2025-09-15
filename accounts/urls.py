# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import create_superuser_temp # Add this import

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/login.html'), name='logout'),
    
    # Add this temporary URL at the end
    path('create-admin-12345/', create_superuser_temp, name='create-superuser-temp'),
]