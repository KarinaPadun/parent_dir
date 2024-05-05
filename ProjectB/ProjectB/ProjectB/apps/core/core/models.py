from django.db import models

class YourModel(models.Model):
    your_field = models.CharField(max_length=100)
    another_field = models.IntegerField()

    def __str__(self):
        return self.your_field
