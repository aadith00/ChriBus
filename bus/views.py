from django.shortcuts import render, get_object_or_404, redirect
from .models import Bus, Booking
from .forms import BusSearchForm, BookingForm


def booking(request):
    return render(request, 'booking.html')

def search_buses(request):
    available_buses = []

    if request.method == 'POST':
        form = BusSearchForm(request.POST)
        if form.is_valid():
            from_city = form.cleaned_data['from_city']
            to_city = form.cleaned_data['to_city']
            date = form.cleaned_data['date']

            # Query the database to get available buses based on search parameters
            available_buses = Bus.objects.filter(departure_city__icontains=from_city, destination_city__icontains=to_city, departure_date=date)

    else:
        form = BusSearchForm()

    return render(request, 'booking.html', {'form': form, 'available_buses': available_buses})


def bus_details(request, num_plate):
    bus = get_object_or_404(Bus, pk=num_plate)
    return render(request, 'bus_details.html', {'bus':bus})


def book_ticket(request, num_plate):
    bus = Bus.objects.get(id=num_plate)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.bus = bus
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'book_ticket.html', {'form': form, 'bus': bus})



