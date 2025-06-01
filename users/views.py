from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.get_full_name() or user.username}!')

            # Redirect based on user role
            if user.is_superuser:
                return redirect('colleges:college_dashboard')
            elif user.is_college_admin:
                return redirect('colleges:college_dashboard')
            elif user.is_teacher:
                return redirect('teachers:dashboard')
            else:
                return redirect('students:dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')

def register_view(request):
    return render(request, 'users/register.html')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})
