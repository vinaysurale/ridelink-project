# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required # Import this

# This is our new home page view
@login_required
def home(request):
    return render(request, 'accounts/home.html')

# This is our existing register view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until admin approval
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created! Please wait for an admin to approve your registration.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})