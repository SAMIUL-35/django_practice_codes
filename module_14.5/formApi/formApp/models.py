from django.db import models

# Create your models here.
class Form(models.Model):  
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)  

    def __str__(self):
        return self.name