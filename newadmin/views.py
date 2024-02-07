from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from bus.models import Bus, Booking

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
    model_data = Booking.objects.values_list('user', 'num_plate', 'journey_date')
    return JsonResponse(list(model_data), safe=False)

