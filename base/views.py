from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def register(request):

    ##    import pdb;                  This is used to pause the page for sometime and 
    ##    pdb.set_trace()              examine the request object so as to check if there are any errors.

    errors = {}
    if request.method == 'POST':

        # first_name = request.POST['first_name'].strip()
        # last_name = request.POST['last_name'].strip()
        register_number = request.POST['register_number'].strip()
        email = request.POST['email'].strip()
        # department = request.POST['department'].strip()
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        cnfpass = request.POST['cnfpass'].strip()

    # ## Validation for first name
    #     if not first_name:
    #         errors['first_name'] = 'First name is required.'

    # ## Validation for last name
    #     if not last_name:
    #         errors['last_name'] = 'Last name is required.'

    ## Validation for Register number
        if not register_number:
            errors['register_number'] = 'Register number is required.'
        else:
            is_used = User.objects.filter(username='register_number').exists()
            if is_used:
                errors['register_number'] = 'Register number already exits.'

    ## Validation for email
        if not email:
            errors['email'] = 'Email field is required.'
        else:
            is_used = User.objects.filter(email='email').exists()
            if is_used:
                errors['email'] = 'This email is already taken.'

    # ## Validation for department
    #     if not department:
    #         errors['department'] = 'Deaprtment is required.'

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

        is_valid = len(errors.keys()) == 0

        if is_valid:

            ## Creating an user

            user = User.objects.create_user(
                # first_name = first_name,
                # last_name = last_name,
                username = register_number,
                email = email,
                # department = department,
                # username = username,
                password = password,
            )
            
            user.save()
            return redirect("/booking")
    
    context = {
        'errors' : errors
    }

    return render (request, "home.html", context) ## Add context argument as well after they complete.


def booking(request):
    return render (request, "booking.html")


def login(request):
    
    if request.method == 'POST':
        register_number =request.POST['register_number']
        password = request.POST['password']

        user = authenticate(request, username=register_number, password=password)

        if user is not None:
            login(request, user)
            return redirect("/booking")
        
        else:
            return redirect("/home")