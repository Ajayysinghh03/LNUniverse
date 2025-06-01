from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def student_dashboard(request):
    return render(request, 'students/dashboard.html')

@login_required
def student_profile(request):
    return render(request, 'students/profile.html')

@login_required
def student_attendance(request):
    return render(request, 'students/attendance.html')

@login_required
def student_marks(request):
    return render(request, 'students/marks.html')
