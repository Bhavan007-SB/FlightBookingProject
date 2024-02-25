from django.contrib import admin
from .models import FlightData,BookingData
# Register your models here.
admin.site.register(FlightData)
admin.site.register(BookingData)