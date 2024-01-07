from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login





def signup(request):

    ##    import pdb;                  This is used to pause the page for sometime and 
    ##    pdb.set_trace()              examine the request object so as to check if there are any errors.

    if request.method == 'POST':
        errors = {}

        first_name = request.POST['first_name'].strip()
        last_name = request.POST['last_name'].strip()
        register_number = request.POST['register_number'].strip()
        department = request.POST['department'].strip()
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        cnfpass = request.POST['cnfpasssword'].strip()
        email = request.POST['email'].strip()

    ## Validation for first name
        if not first_name:
            errors['first_name'] = 'First name is required.'

    ## Validation for last name
        if not last_name:
            errors['last_name'] = 'Last name is required.'

    ## Validation for Register number
        if not register_number:
            errors['register_number'] = 'Register number is required.'
        else:
            is_used = User.objects.filter(register_number='register_number').exists()
            if is_used:
                errors['register_number'] = 'Register number already exits.'

    ## Validation for department
        if not department:
            errors['department'] = 'Deaprtment is required.'

    ## Validation for username
        if not username:
            errors['username'] = 'Username field is required.'
        else:
            is_used = User.objects.filter(username='username').exists()
            if is_used:
                errors['username'] = 'This username is already taken.'

    ## Validation for password
        if not password:
            errors['password'] = 'Password is required.'
        if not cnfpass:
            errors['cnfpass'] = 'Password is required.'
        if password != cnfpass:
            errors['password'] = 'The passwords do not match.'

    ## Validation for email
        if not email:
            errors['email'] = 'Email field is required.'
        else:
            is_used = User.objects.filter(email='email').exists()
            if is_used:
                errors['email'] = 'This email is already taken.'

        is_valid = len(errors.keys()) == 0
        if is_valid:
            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                register_number = register_number,
                department = department,
                username = username,
                password = password,
            )
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/?signup=successfull')
    
    context = {
        'errors' : errors
    }

    return render (request, "signup.html", context)

def booking(request):
    return render (request, "booking.html")