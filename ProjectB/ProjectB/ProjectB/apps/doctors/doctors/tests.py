from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Doctor

class DoctorModelTestCase(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
            username='test_doctor',
            password='test_password',
            specialization='Test Specialization',
        )

    def test_doctor_creation(self):
        self.assertEqual(self.doctor.username, 'test_doctor')
        self.assertEqual(self.doctor.specialization, 'Test Specialization')

class DoctorAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.doctor_data = {
            'username': 'test_doctor_api',
            'password': 'test_password_api',
            'specialization': 'Test API Specialization',
        }
        self.response = self.client.post(reverse('doctor-list'), self.doctor_data, format='json')

    def test_api_create_doctor(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_get_doctor_list(self):
        response = self.client.get(reverse('doctor-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
