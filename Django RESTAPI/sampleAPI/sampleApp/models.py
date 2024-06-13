from django.db import models

# Create your models here.

class Sample(models.Model):
    Sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length=30)
    about = models.TextField()
    type = models.CharField(choices=(('IT','IT'),('Non-IT','Non-IT')), max_length=50)
    added_date = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)
    # def __str__(self):
    #     return self.name
    

class Employee(models.Model):
    Eid = models.AutoField(primary_key=True)
    Name = models.CharField(max_length =30)
    email = models.EmailField(max_length=254)
    contactno = models.CharField(max_length = 10)
    address = models.TextField()
    company_name = models.ForeignKey(Sample,on_delete = models.CASCADE)
    position = models.CharField(choices = (
        ('Manager', 'Manager'),
        ('HR','HR'),
        ('Software Engineer','SE'),
        ('Project lead','Project lead')
    ),max_length = 30)
    # def __str__(self):
    #     return super().__str__()
    
    