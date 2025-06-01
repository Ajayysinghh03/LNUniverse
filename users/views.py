from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    return render(request, 'users/login.html')

def register_view(request):
    return render(request, 'users/register.html')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')
