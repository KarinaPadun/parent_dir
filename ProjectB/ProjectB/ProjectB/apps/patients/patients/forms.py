from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'date_of_birth', 'gender', 'email', 'phone_number']
        labels = {
            'name': 'ФИО',
            'date_of_birth': 'Дата рождения',
            'gender': 'Пол',
            'email': 'Email',
            'phone_number': 'Номер телефона'
        }
