from django.db import models

# Create your models here
class student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=50)
#    sclass=models.IntegerField()
    saddress=models.CharField(max_length=100)
    
