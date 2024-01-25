from django.shortcuts import render

def rentals(request):
    return render(request, 'index.html')

def support(request):
    return render(request, 'contact_copy.html')

def register(request):
    return render(request, 'register.html')
