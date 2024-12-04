from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    gender = models.CharField(max_length=30, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others','Others')], default='Male')
    ph_num = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
