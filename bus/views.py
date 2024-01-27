from django.shortcuts import render
from .models import bus
from .forms import BusSearchForm


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
            available_buses = bus.objects.filter(departure_city__icontains=from_city, destination_city__icontains=to_city, departure_date=date)

    else:
        form = BusSearchForm()

    return render(request, 'booking.html', {'form': form, 'available_buses': available_buses})
