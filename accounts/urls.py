# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Add our new home page URL
    path('', views.home, name='home'), 
    
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # For logout, we'll redirect to the login page
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/login.html'), name='logout'),
]