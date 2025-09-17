# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import get_user_model

@login_required
def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created! Please wait for an admin to approve your registration.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
# Add these imports at the top of the file if they are not there
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# Add this new function at the very bottom
def create_new_superuser_temp(request):
    User = get_user_model()
    # Let's use a new username to be safe
    if not User.objects.filter(username='superuser').exists():
        User.objects.create_superuser('superuser', 'super@user.com', 'superpassword123')
        return HttpResponse("New superuser account created! Username: superuser, Password: superpassword123")
    return HttpResponse("New superuser account already exists.")