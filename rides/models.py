# rides/models.py
from django.db import models
# We no longer need to import User directly, we'll use a setting
from django.conf import settings

class Ride(models.Model):
    VEHICLE_CHOICES = [
        ('Car', 'Car'),
        ('Bike', 'Bike'),
    ]

    # This line is now changed to point to the new User model
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    ride_datetime = models.DateTimeField()
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_CHOICES)
    seats_available = models.PositiveIntegerField()
    fare = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.from_location} to {self.to_location} on {self.ride_datetime.strftime("%Y-%m-%d")}'

# Your Review model (if it exists) also needs this change if it links to a user
# (We will add the Review model later, so no changes needed for now)