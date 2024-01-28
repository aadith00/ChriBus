from django.shortcuts import render,redirect
from .models import rent
from django.contrib.auth.models import User,auth

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

def upload(request):
    if request.method == 'POST':
        owners_name = request.POST['owners_name']
        vehicle_model = request.POST['vehicle_model']
        rental_price = request.POST['rental_price']
        image = request.POST['image']

        user = User.objects.create_user(owners_name=owners_name,vehicle_model=vehicle_model,rental_price=rental_price,image=image)
        user.save();
        print('user creataed')
        return redirect('/')

    else:
        return render(request,'upload.html')    

def contact(request):
    return render(request,'contact.html')