"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.base_view, name='home'),
    path('patients/', views.patients_list, name='patients_list'),
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('patient/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('doctor/<int:pk>/', views.doctor_detail, name='doctor_detail'),
]

