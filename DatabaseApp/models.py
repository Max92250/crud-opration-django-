from email.policy import default
from django.db import models
from django.urls import reverse


# Create your models here.
class Employee(models.Model):  
    eid      = models.CharField(max_length=20)  
    ename    = models.CharField(max_length=100)  
    econtact = models.CharField(max_length=15)  
  
    image = models.ImageField(upload_to='images')
    class Meta:  
        db_table = "employee"  