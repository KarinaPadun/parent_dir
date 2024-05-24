
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html')


class PatientListView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patients_list.html', {'patients': patients})


@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patients/patient_detail.html', {'patient': patient})
