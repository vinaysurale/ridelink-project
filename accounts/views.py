# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm # Changed this line
from django.contrib.auth.decorators import login_required
# ... (keep any other functions you have like home, etc.)

@login_required
def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) # Changed this line
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created! Please wait for an admin to approve your registration.')
            return redirect('login')
    else:
        form = CustomUserCreationForm() # Changed this line
    return render(request, 'accounts/register.html', {'form': form})