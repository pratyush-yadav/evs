from django.db import models

# Create your models here.
class Voters(models.Model):
    voter_id = models.CharField(max_length=10)
    aadhar = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=6)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.voter_id} {self.name}"
