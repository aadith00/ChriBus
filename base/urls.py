from django.urls import path
from .views import home,bookings


urlpatterns = [
    path('', home),
    path('booking', bookings)
]