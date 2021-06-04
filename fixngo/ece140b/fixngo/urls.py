from os import name
from django.urls import path
from . import views

app_name = 'fixngo'

urlpatterns = [
    path('', views.home, name='home page'),
    path('register/', views.register, name='register page'),
    path('profile/', views.profile, name='profile page'),
    path('soft_review/<int:repair_id>/', views.soft_review, name='reivew page'),
    path('hard_review/<int:repair_id>/', views.hard_review, name='reivew page'),
    path('soft_post_review/<int:repair_id>/', views.soft_post_review, name='post reivew page'),
    path('hard_post_review/<int:repair_id>/', views.hard_post_review, name='post reivew page'),
    path('software/', views.software, name='software'),
    path('software/<int:repair_id>/', views.s_repair_detail, name='SoftwareDetailedRequest'),
    path('hardware/', views.hardware, name='hardware'),
    path('hardware/<int:repair_id>/', views.h_repair_detail, name='HardwareDetailedRequest'),
    path('myrepairs/', views.repairs, name='my repairs page')
]