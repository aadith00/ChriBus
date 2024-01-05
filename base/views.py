from django.shortcuts import render

def signup(request):
    return render (request, "signup.html")

def booking(request):
    return render (request, "booking.html")