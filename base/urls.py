from django.urls import path
from .views import register,booking,login


urlpatterns = [
    path('', register),
    path('register', register),
    path('login', login),
    path('booking', booking),
]