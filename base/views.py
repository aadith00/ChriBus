from django.shortcuts import render

def home(request):
    return render (request, "home.html")

def bookings(request):
    return render (request, "bookings.html")