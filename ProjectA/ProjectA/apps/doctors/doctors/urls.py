"""
URL configuration for doctors project.

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
from django.urls import path
from .views import (
    DoctorListView,
    DoctorDetailView,
    DoctorCreateView,
    DoctorUpdateView,
    DoctorDeleteView,
    AppointmentListView,
    AppointmentDetailView,
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView,
)

urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name='doctors_list'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctor/create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctor/<int:pk>/update/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctor/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor_delete'),

    path('appointments/', AppointmentListView.as_view(), name='appointments_list'),
    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointment/create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointment/<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointment/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),
]
