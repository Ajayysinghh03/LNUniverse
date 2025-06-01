from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def college_list(request):
    return render(request, 'colleges/college_list.html')

@login_required
def college_detail(request, college_id):
    return render(request, 'colleges/college_detail.html')

@login_required
def college_dashboard(request):
    return render(request, 'colleges/college_dashboard.html')
