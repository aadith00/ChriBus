from django.urls import path
from .views import register,booking,login


urlpatterns = [
    path('', register),
    path('home', register),
    path('home', login),
    path('booking', booking),
    
]