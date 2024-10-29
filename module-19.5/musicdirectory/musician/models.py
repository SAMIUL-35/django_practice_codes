from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Musicmodel(models.Model):
    first_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    
    
    INSTRUMENT_CHOICES = [
        ('Guitar', 'Guitar'),
        ('Piano', 'Piano'),
        ('Drums', 'Drums'),
        ('Violin', 'Violin'),
    ]
    Instrument_Type = models.CharField(max_length=50, choices=INSTRUMENT_CHOICES)

    def __str__(self):
        return f"{self.first_Name} {self.last_Name}"
