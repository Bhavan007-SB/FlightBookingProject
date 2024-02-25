from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FlightData(models.Model):
    flightNumber = models.CharField(max_length=10)
    flightName = models.CharField(max_length=50)
    journeyDate = models.DateField()
    depatureTime = models.TimeField()
    arrivalTime = models.TimeField()
    flightFrom = models.CharField(max_length=50)
    flightTo = models.CharField(max_length=50)
    seatcount = models.IntegerField(default=60)
    flightobject = models.Manager()

    def __str__(self):
        return self.flightName +' | '+ self.flightNumber

class BookingData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    flight = models.ForeignKey(FlightData,on_delete=models.CASCADE)
    num_seats = models.IntegerField(default=1)
    bookingobject = models.Manager()