from django.test import TestCase
from .models import Patient

class PatientModelTest(TestCase):
    def setUp(self):
        Patient.objects.create(name='John Doe', date_of_birth='1990-01-01')

    def test_patient_creation(self):
        patient = Patient.objects.get(name='John Doe')
        self.assertEqual(patient.name, 'John Doe')
        self.assertEqual(patient.date_of_birth, '1990-01-01')

