from django.urls import path
from .views import sigin_home, booking, register, login, logout


urlpatterns = [
    # path('', register),
    # path('home',register),
    # path('register', register),
    # path('login', login),
    # path('booking', booking),
    # path('home', logout)

    path('', register),
    path('home', sigin_home),
    path('register', register),
    path('login', login),
    path('booking', booking),
    path('home', logout)

]