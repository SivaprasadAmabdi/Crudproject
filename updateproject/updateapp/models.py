from django.db import models

# Create your models here.
class Amodel(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=250)
