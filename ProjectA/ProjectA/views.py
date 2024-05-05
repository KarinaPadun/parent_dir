from django.http import JsonResponse
from myapp.tasks import calculate_something
from django.shortcuts import render
from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer

def home(request):
    return render(request, 'home.html')

class PatientListView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

def my_view(request):
    result = calculate_something.delay(2, 3)
    return JsonResponse({'task_id': result.id})
