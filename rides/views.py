# rides/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RideCreationForm
from .models import Ride

# This is our new view for showing a user's own rides
@login_required
def my_rides(request):
    # Filter the rides to get only the ones where the driver is the current user
    rides = Ride.objects.filter(driver=request.user).order_by('-ride_datetime')
    return render(request, 'rides/my_rides.html', {'rides': rides})

@login_required
def find_ride(request):
    rides = Ride.objects.all().order_by('ride_datetime')
    return render(request, 'rides/find_ride.html', {'rides': rides})

@login_required
def post_ride(request):
    if request.method == 'POST':
        form = RideCreationForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.driver = request.user
            ride.save()
            messages.success(request, 'Your ride has been posted successfully!')
            return redirect('home')
    else:
        form = RideCreationForm()
        
    return render(request, 'rides/post_ride.html', {'form': form})