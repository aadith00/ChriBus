from django.shortcuts import render
from django.contrib.auth.models import User
from bus.models import Bus, Booking

def dashboard(request):
    bus_data = Bus.objects.all()

    user_count = User.objects.all().count()
    labels = [bus.num_plate for bus in bus_data]
    data_values = [bus.total_seats-bus.booked_seats for bus in bus_data]
    
    context = {
        'labels' : labels,
        'data_values' : data_values,
        'user_count': user_count,
    }

    return render(request, 'dashboard.html', context)

# def bus_chart(request):
#     bus_data = Bus.objects.all()

#     user_count = User.objects.all().count()
#     labels = [bus.num_plate for bus in bus_data]
#     data_values = [bus.total_seats-bus.booked_seats for bus in bus_data]
    
#     context = {
#         'labels' : labels,
#         'data_values' : data_values,
#         'user_count': user_count,
#     }

#     return render(request, 'dashboard.html', context)
