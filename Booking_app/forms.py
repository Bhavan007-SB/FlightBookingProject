from django import forms
from .models import FlightData

class AddFlightForm(forms.ModelForm):
    class Meta:
        model = FlightData
        fields = "__all__"

    widgets = {
        "flightNumber" : forms.TextInput(attrs={"class":"form-control"}),
        "flightName": forms.TextInput(attrs={"class": "form-control"}),
        "journeyDate": forms.DateInput(attrs={"class": "form-control"}),
        "depatureTime": forms.TimeInput(attrs={"class": "form-control"}),
        "arrivalTime": forms.TimeInput(attrs={"class": "form-control"}),
        "flightFrom": forms.TextInput(attrs={"class": "form-control"}),
        "flightTo": forms.TextInput(attrs={"class": "form-control"}),
        "seatcount": forms.NumberInput(attrs={"class": "form-control"}),
    }

class BookingForm(forms.Form):
    num_seats = forms.IntegerField(min_value=1,label='Number of Seats')

class SearchForm(forms.Form):
    depature_date = forms.DateField()
    depature_time = forms.TimeField()