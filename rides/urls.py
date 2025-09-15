# rides/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_ride, name='post-ride'),
    path('find/', views.find_ride, name='find-ride'),
    path('my-rides/', views.my_rides, name='my-rides'), # Add this line
]