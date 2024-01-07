from django.shortcuts import render

def signup(request):
    print(request.method)

##    import pdb;                   This is used to pause the page for sometime and examine the request object so as to check if there are any errors.
##    pdb.set_trace()




    return render (request, "signup.html")

def booking(request):
    return render (request, "booking.html")