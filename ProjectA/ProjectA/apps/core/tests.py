from django.test import TestCase
from .models import BaseModel


class BaseModelTest(TestCase):
    def test_created_at_and_updated_at_fields(self):
        base_model = BaseModel()
        base_model.save()

        self.assertTrue(base_model.created_at is not None)
        self.assertTrue(base_model.updated_at is not None)

        base_model.first_name = 'John'
        base_model.save()

        self.assertEqual(base_model.created_at, base_model.updated_at)

        base_model.updated_at = base_model.updated_at + datetime.timedelta(seconds=1)
        base_model.save()

        self.assertNotEqual(base_model.created_at, base_model.updated_at)
