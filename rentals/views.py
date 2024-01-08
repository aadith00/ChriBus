from django.shortcuts import render

def rentals(request):
    return render(request, 'index.html')
