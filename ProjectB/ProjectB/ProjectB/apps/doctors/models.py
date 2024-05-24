from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.username


class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=100)
    

    def __str__(self):
        return self.user.username
