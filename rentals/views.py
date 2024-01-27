from django.shortcuts import render
from .models import rent

def index(request):
    rent1 = rent()
    rent1.name = 'Suzuki Brezza'
    rent1.price = 1850

    rent2 = rent()
    rent2.name = "XUV 700"
    rent2.price = 2200

    rent3 = rent()
    rent3.name = "RE Scrambler"
    rent3.price = 1550

    return render(request, 'index.html',({'rent1': rent1,'rent2': rent2,'rent3': rent3}))

def contact(request):
    return render(request,'contact.html')