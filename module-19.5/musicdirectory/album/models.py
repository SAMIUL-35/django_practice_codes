from django.db import models
from musician.models import Musicmodel 
from datetime import date 
class Albummodel(models.Model):
    Name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musicmodel, on_delete=models.CASCADE) 
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)  
    release_date = models.DateField(default=date.today)  

    def __str__(self):
        return self.Name
