from django.shortcuts import render, redirect, get_object_or_404
from .models import Bus, Booking
from datetime import datetime
import random


def booking(request):
    return render(request, 'booking.html')

def search_buses(request):
    if request.method == 'POST':
        departure_city = request.POST.get('departureCity')
        destination_city = request.POST.get('destinationCity')
        departure_date_str = request.POST.get('departureDate')

        if departure_date_str:
            departure_date = datetime.strptime(departure_date_str, '%Y-%m-%d').date()

        available_buses = Bus.objects.filter(departure_city=departure_city, destination_city=destination_city, departure_date=departure_date)

        return render(request, 'buses_list.html', {'available_buses': available_buses})
    
    else:
        return render(request, 'no_buses.html')

    # return render(request, 'booking.html')  


def bus_details(request, num_plate):
    bus = get_object_or_404(Bus, pk=num_plate)
    bus.available_seats = bus.calculate_available_seats()

    bus.tick_num = bus.generate_random_ticket()

    return render(request, 'bus_details.html', {'bus':bus})


def book_ticket(request, num_plate, tick_num):
    if request.method == 'POST':

        # Retrieve the bus instance
        bus = Bus.objects.get(pk=num_plate)
        bus.booked_seats += 1
        bus.save()
        
        booking = Booking.objects.create(
            user=request.user,
            num_plate=bus,
            ticket_number = tick_num,
            journey_date = bus.departure_date
        )

        if not booking.journey_date:
            booking.journey_date = datetime.now().date()

        booking.save()

        return render(request, 'book_success.html')
    else:
        return render(request, 'book_failure.html')  # Handle case when no available seats


