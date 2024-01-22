from django.urls import path
from .views import register, booking, login, logout


urlpatterns = [
    path('', register),
    path('home',register),
    path('register', register),
    path('login', login),
    path('booking', booking),
    path('logout', logout)
]