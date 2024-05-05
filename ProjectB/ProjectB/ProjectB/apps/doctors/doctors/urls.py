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
from . import views

app_name = 'doctors'

urlpatterns = [
    path('list/', views.DoctorListView.as_view(), name='doctor-list'),
    path('detail/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('create/', views.DoctorCreateView.as_view(), name='doctor-create'),
    path('update/<int:pk>/', views.DoctorUpdateView.as_view(), name='doctor-update'),
    path('delete/<int:pk>/', views.DoctorDeleteView.as_view(), name='doctor-delete'),
]
