from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='dashboard'),
    path('profile/', views.student_profile, name='profile'),
    path('attendance/', views.student_attendance, name='attendance'),
    path('marks/', views.student_marks, name='marks'),
]