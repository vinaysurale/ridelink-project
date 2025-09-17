# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/login.html'), name='logout'),
]
# accounts/urls.py
# ... (keep all your existing code) ...
from .views import create_new_superuser_temp # Add this new import

urlpatterns = [
    # ... (keep your existing URLs) ...
    
    # Add this new temporary URL at the end
    path('make-new-admin-9876/', create_new_superuser_temp, name='create-new-superuser'),
]