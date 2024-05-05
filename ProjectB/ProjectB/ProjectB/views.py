from rest_framework import generics, status
from rest_framework.response import Response
from .models import Patient, Doctor
from .serializers import PatientSerializer, DoctorSerializer
from myapp.tasks import send_message

class PatientListView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        send_message.delay('user@example.com', 'New patient created!')
        return super().create(request, *args, **kwargs)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorListView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def create(self, request, *args, **kwargs):
        send_message.delay('user@example.com', 'New doctor created!')
        return super().create(request, *args, **kwargs)

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
