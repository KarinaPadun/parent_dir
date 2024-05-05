"""
URL configuration for patients project.

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

app_name = 'patients'

urlpatterns = [
    path('patients/', views.PatientListView.as_view(), name='patient-list'),
    path('patients/create/', views.PatientCreateView.as_view(), name='patient-create'),
    path('patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('patients/<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient-update'),
    path('patients/<int:pk>/delete/', views.PatientDeleteView.as_view(), name='patient-delete'),
]

