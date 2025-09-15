# rides/forms.py
from django import forms
from .models import Ride

class RideCreationForm(forms.ModelForm):
    class Meta:
        model = Ride
        # We don't include the 'driver' field here because
        # we'll set the driver automatically to the logged-in user.
        fields = [
            'from_location', 'to_location', 'ride_datetime', 
            'vehicle_type', 'seats_available', 'fare'
        ]
        widgets = {
            'ride_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }