from django.test import TestCase
from .models import Patient

class PatientModelTest(TestCase):
    def test_create_patient(self):
        patient = Patient.objects.create(first_name='John', last_name='Doe', email='johndoe@example.com', phone_number='+380971234567')
        self.assertEqual(patient.first_name, 'John')
        self.assertEqual(patient.last_name, 'Doe')
        self.assertEqual(patient.email, 'johndoe@example.com')
        self.assertEqual(patient.phone_number, '+380971234567')

    def test_email_unique(self):
        patient1 = Patient.objects.create(first_name='John', last_name='Doe', email='johndoe@example.com', phone_number='+380971234567')
        with self.assertRaises(ValidationError):
            patient2 = Patient.objects.create(first_name='Jane', last_name='Doe', email='johndoe@example.com', phone_number='+380987654321')

