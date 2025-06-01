from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('dashboard/', views.teacher_dashboard, name='dashboard'),
    path('profile/', views.teacher_profile, name='profile'),
    path('attendance/', views.manage_attendance, name='attendance'),
    path('marks/', views.manage_marks, name='marks'),
]