from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect

def admin_login(request):
    
    try:
        if request.user.is_authenticated:
            return redirect('/dashboard')
        
        # messages.info(request, 'Account not found')
        
        if request.method == 'POST':
            register_number = request.POST.get('register_number')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username = register_number)

            if not user_obj.exists():
                messages.info(request, 'Account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            user_obj = authenticate(username = register_number , password = password)

            if user_obj and user_obj.is_superuser:
                login(request , user_obj)
                return redirect('/dashboard')

            messages.info(request, 'Invalid password')
            return redirect('/')

        return render(request, 'admin_login.html')

    except Exception as e:
        print(e)