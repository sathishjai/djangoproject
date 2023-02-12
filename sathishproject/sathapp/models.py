from django.db import models

# Create your models here.
class sathishjai(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=50)
    sclass=models.IntegerField()
    sadderss=models.CharField(max_length=100)
