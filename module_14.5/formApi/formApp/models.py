from django.db import models
from django.utils import timezone

class Form(models.Model):  
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=128)  
    birth_date = models.DateField(default=timezone.now)
    value = models.DecimalField(max_digits=10, decimal_places=2)  
    auto_field = models.AutoField(primary_key=True)
    
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    duration_field = models.DurationField()
    file_field = models.FileField(upload_to='files/')
    ile_path_field = models.FilePathField(path='/path/to/files/')
    image_field = models.ImageField(upload_to='images/')
    slug_field = models.SlugField()


    def __str__(self):
        return self.name
