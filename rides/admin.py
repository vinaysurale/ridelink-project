# rides/admin.py
from django.contrib import admin
from .models import Ride  # Import our Ride model

# Register your models here.
admin.site.register(Ride)