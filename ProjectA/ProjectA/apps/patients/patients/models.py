from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
