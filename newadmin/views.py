from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from bus.models import Bus, Booking
from django.core.serializers import serialize
from django.forms.models import model_to_dict

def index(request):
    return render(request, 'adminlogin.html')

def dashboard(request):
    bus_data = Bus.objects.all()

    bus_count = Bus.objects.all().count()
    user_count = User.objects.all().count()
    labels = [bus.num_plate for bus in bus_data]
    data_values = [bus.total_seats-bus.booked_seats for bus in bus_data]
    booking_count = Booking.objects.all().count()
    
    context = {
        'labels' : labels,
        'data_values' : data_values,
        'user_count': user_count,
        'booking_count':booking_count,
        'bus_count':bus_count
    }

    return render(request, 'dashboard.html', context)


def get_model_data(request):
    tickets = Booking.objects.all()
    data = []

    for item in tickets:
        # Convert User object to dictionary
        user_dict = model_to_dict(item.user)
        # Extract necessary fields from the user dictionary
        username = user_dict.get('username', '')
        
        data.append([username, item.num_plate, item.ticket_number, item.journey_date])
        
    return JsonResponse({
        "data": data
    })