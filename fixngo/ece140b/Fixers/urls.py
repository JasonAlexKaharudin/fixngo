from django.urls import path
from . import views

app_name = 'Fixers'

urlpatterns = [
    path('fixers/', views.dashboard, name='dashboard'),
    path('softwarejob/<int:job_id>/', views.software_jobs, name='job list'),
    path('hardwarejob/<int:job_id>/', views.hardware_jobs, name='job list'),
    path('jobs/', views.jobs, name='job list'),
    path('finishSoftJob/<int:job_id>/', views.finishSoftJob, name='list job as done'),
    path('finishHardJob/<int:job_id>/', views.finishHardJob, name='list job as done'),
]