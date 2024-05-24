# ProjectA/doctors/views.py

from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer

# Функция для отображения списка врачей
class DoctorListView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# Функция для отображения детальной информации о враче
class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctors_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})
