from django.db import models

# Create your models here.
#  Creating Company model

class Company(models.Model):
    Company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=[('MNC', 'MNC'), ('Startup', 'Startup')])
    added_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
