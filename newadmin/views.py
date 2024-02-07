from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from bus.models import Bus, Booking
from django.contrib.auth import authenticate, login, logout

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
    tickets = Booking.objects.all()[:50]
    data = []

    for item in tickets:
        data.append([str(item.user.username), str(item.num_plate), str(item.ticket_number), str(item.journey_date)])
        
    return JsonResponse({
        "data": data
    })


def admin_login(request):
    if request.method == 'POST':
        admin_username = request.POST.get('adminuser')
        password = request.POST.get('password')

        user = authenticate(request, username=admin_username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return render(request, 'dashboard.html')
        else:
            error_message = "Invalid admin credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})


    return render(request, 'login.html')


def admin_logout(request):
    logout(request)
    return redirect('/newadmin')