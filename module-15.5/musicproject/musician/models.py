from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
