from django.test import TestCase
from .models import Doctor, Appointment

class DoctorModelTest(TestCase):
    def test_create_doctor(self):
        doctor = Doctor.objects.create(name='John Doe', specialty='Cardiologist', email='johndoe@example.com', phone_number='+380971234567')
        self.assertEqual(doctor.name, 'John Doe')
        self.assertEqual(doctor.specialty, 'Cardiologist')
        self.assertEqual(doctor.email, 'johndoe@example.com')
        self.assertEqual(doctor.phone_number, '+380971234567')

class AppointmentModelTest(TestCase):
    def test_create_appointment(self):
        patient = Patient.objects.create(first_name='Jane', last_name='Doe', email='janedoe@example.com', phone_number='+380987654321')
        doctor = Doctor.objects.create(name='John Doe', specialty='Cardiologist', email='johndoe@example.com', phone_number='+380971234567')
        appointment = Appointment.objects.create(patient=patient, doctor=doctor, date='2023-12-31', time='10:00:00', description='Regular checkup')
        self.assertEqual(appointment.patient, patient)
        self.assertEqual(appointment.doctor, doctor)
        self.assertEqual(appointment.date, '2023-12-31')
        self.assertEqual(appointment.time, '10:00:00')
        self.assertEqual(appointment.description, 'Regular checkup')
