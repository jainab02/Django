from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Finance(models.Model):
    # user = models.ForeignKey(User,on_delete = models.SET_NULL,blank=True, null=True)
    name= models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    budget = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    