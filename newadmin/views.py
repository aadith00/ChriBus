from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def tables(request):
    return render(request, 'datatables.html')