from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import YourModel

class YourModelTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_your_model(self):
        url = reverse('your-model-list')
        data = {'your_field': 'Test', 'another_field': 123}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(YourModel.objects.count(), 1)
        self.assertEqual(YourModel.objects.get().your_field, 'Test')

    def test_get_your_model(self):
        instance = YourModel.objects.create(your_field='Test', another_field=123)
        url = reverse('your-model-detail', kwargs={'pk': instance.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['your_field'], 'Test')

    

