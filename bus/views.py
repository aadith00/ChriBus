from django.shortcuts import render, redirect, get_object_or_404
from .models import Bus
from datetime import datetime


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
    return render(request, 'bus_details.html', {'bus':bus})



# def book_ticket(request, num_plate):
#     bus = Bus.objects.get(id=num_plate)
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.bus = bus
#             booking.user = request.user
#             booking.save()
#             return redirect('booking_success')
#     else:
#         form = BookingForm()
#     return render(request, 'book_ticket.html', {'form': form, 'bus': bus})


