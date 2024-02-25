from django.urls import path
from .views import Home,AddFlights,FlightDetail,FlightUpdate,FlightDelete,AdminPage,Registerview,MyBookings,Booking
urlpatterns = [
    path('register/',Registerview.as_view(),name='register'),
    path("",Home.as_view(),name="home"),
    path("adminpage/",AdminPage.as_view(),name="adminpage"),
    path("addfights/",AddFlights.as_view(),name="addflights"),
    path("flightdetails/<int:pk>",FlightDetail.as_view(),name="flightdetails"),
    path("flightupdate/<int:pk>",FlightUpdate.as_view(),name="flightupdate"),
    path("flightdelete/<int:pk>",FlightDelete.as_view(),name="flightdelete"),
    path("booking/<int:pk>/",Booking.as_view(),name="boooking"),
    path("mybookings/",MyBookings.as_view(),name="mybookings")
]