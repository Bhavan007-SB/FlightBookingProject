from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView,FormView
from django.contrib.auth.forms import UserCreationForm
from .models import FlightData,BookingData
from .forms import AddFlightForm,BookingForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
# Create your views here


class Registerview(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class Home(ListView):
    model = FlightData
    template_name = 'home.html'
    context_object_name = 'flights'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_date = self.request.GET.get('search-date') or ''
        search_time = self.request.GET.get('search-time') or ''
        if search_date or search_time :
            context['flights'] = context['flights'].filter(journeyDate__icontains=search_date,depatureTime__icontains=search_time)
        context['search_date'] = search_date
        context['search_time'] = search_time

        return context

@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdminPage(ListView):
    model = FlightData
    template_name = 'adminpage.html'
    context_object_name = 'flights'

@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
@method_decorator(login_required, name='dispatch')
class AddFlights(CreateView):
    model = FlightData
    template_name = 'addflights.html'
    form_class = AddFlightForm
    success_url = reverse_lazy('adminpage')

@method_decorator(login_required, name='dispatch')
class FlightDetail(DetailView):
    model = FlightData
    template_name = 'flightdetails.html'
    context_object_name = 'flights'

@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
@method_decorator(login_required, name='dispatch')
class FlightUpdate(UpdateView):
    model = FlightData
    template_name =  'flightupdate.html'
    form_class = AddFlightForm
    success_url = reverse_lazy('adminpage')

@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
@method_decorator(login_required, name='dispatch')
class FlightDelete(DeleteView):
    model = FlightData
    template_name = 'flightdelete.html'
    success_url = reverse_lazy('adminpage')

@method_decorator(login_required, name='dispatch')
class Booking(FormView):
    template_name = 'booking.html'
    form_class = BookingForm
    success_url = reverse_lazy('mybookings')


    def form_valid(self, form):
        flight_id = self.kwargs['pk']
        flight = FlightData.flightobject.get(id=flight_id)
        num_seats = form.cleaned_data['num_seats']

        if num_seats <= flight.seatcount:
            booking = BookingData.bookingobject.create(user=self.request.user, flight=flight, num_seats=num_seats)
            flight.seatcount -= num_seats
            flight.save()
            return super().form_valid(form)
        else:
            form.add_error('num_seats', 'Not enough seats available')
            return self.form_invalid(form)

@method_decorator(login_required, name='dispatch')
class MyBookings(ListView):
    model = BookingData
    template_name = 'mybookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return BookingData.bookingobject.filter(user=self.request.user)