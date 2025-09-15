# rides/models.py
from django.db import models
from django.contrib.auth.models import User

class Ride(models.Model):
    # Choices for the vehicle type field
    VEHICLE_CHOICES = [
        ('Car', 'Car'),
        ('Bike', 'Bike'),
    ]

    # This links the ride to the user who is driving
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Basic ride information
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    ride_datetime = models.DateTimeField()
    
    # Ride details
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_CHOICES)
    seats_available = models.PositiveIntegerField()
    fare = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.from_location} to {self.to_location} on {self.ride_datetime.strftime("%Y-%m-%d")}'