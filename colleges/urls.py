from django.urls import path
from . import views

app_name = 'colleges'

urlpatterns = [
    path('', views.college_list, name='list'),
    path('<int:college_id>/', views.college_detail, name='detail'),
    path('dashboard/', views.college_dashboard, name='dashboard'),
]