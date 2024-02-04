from django.shortcuts import render
from bus.models import Bus, Booking

def dashboard(request):
    return render(request, 'dashboard.html')

def tables(request):
    return render(request, 'datatables.html')

def bus_chart(request):
    data = Bus.objects.all()
    data_for_chart = [{'x': entry.field1, 'y': entry.field2} for entry in data]

    return render(request, 'dashboard.html', {'data_for_chart':data_for_chart})