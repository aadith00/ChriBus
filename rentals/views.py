from django.shortcuts import render,redirect
from .models import rent,VehicleRental
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

def register(request):
    return render(request,'register.html')

def bullet(request):
    return render(request,'bullet.html')

def toyota(request):
    return render(request,'toyota.html')

def bikerental(request):
    return render(request,'bikerental.html')

def rent_details(request):
    return render(request,'rent-details.html')


def submit_form(request):
    if request.method == 'POST':
        owner_name = request.POST.get('ownerName')
        vehicle_type = request.POST.get('vehicleType')
        vehicle_model = request.POST.get('vehicleModel')
        rental_price = request.POST.get('rentalPrice')
        image_upload = request.FILES.get('imageUpload')

        # Save data to the database
        rental = VehicleRental.objects.create(
            ownerName=owner_name,
            vehicleType=vehicle_type,
            vehicleModel=vehicle_model,
            rentalPrice=rental_price,
            imageUpload=image_upload
        )
        rental.save()

        return render(request, 'success.html')  # Redirect to a success page or any other page
    return render(request, 'upload.html')  # Replace 'your_template.html' with your actual template file

# def success_page(request):
#     return render(request, 'success.html')