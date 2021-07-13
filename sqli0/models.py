from django.db import models
from datetime import datetime

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phoneno = models.IntegerField()
    date_of_birth = models.DateField(default=datetime.now)
    password = models.CharField(max_length=4)
    