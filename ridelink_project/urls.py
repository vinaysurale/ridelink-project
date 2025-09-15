# ridelink_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rides/', include('rides.urls')), # Add this line
    path('', include('accounts.urls')),
]