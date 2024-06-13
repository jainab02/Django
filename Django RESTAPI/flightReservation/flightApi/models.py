from django.db import models

# Create your models here.

class Flight(models.Model):
    flightNumber =models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=30)
    departureCity = models.CharField(max_length=30)
    arrivalCity = models.CharField(max_length=30)
    departureDate = models.DateField()
    estTimeofDep = models.TimeField()


class Passenger(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    MidName = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

class Reservation(models.Model):
    flight = models.ForeignKey(Flight,on_delete =models.CASCADE)
    passenger = models.OneToOneField(Passenger,on_delete =models.CASCADE)
