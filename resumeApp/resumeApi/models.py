from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    dob = models.DateField(auto_now = False,auto_now_add = False)
    state = models.CharField(max_length= 50)
    gender = models.CharField(max_length= 50)
    location = models.CharField(max_length= 50)
    profimage = models.ImageField(upload_to='media/resumeImages',blank= True)
    resumeDoc = models.FileField(upload_to='media/resumeDocs',blank= True)

