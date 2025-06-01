from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def teacher_dashboard(request):
    return render(request, 'teachers/dashboard.html')

@login_required
def teacher_profile(request):
    return render(request, 'teachers/profile.html')

@login_required
def manage_attendance(request):
    return render(request, 'teachers/manage_attendance.html')

@login_required
def manage_marks(request):
    return render(request, 'teachers/manage_marks.html')
