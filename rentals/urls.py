from django.urls import path,include
from .views import rentals, support, register

urlpatterns = [
    path('rentals', rentals),
    path('register', register),
    path('support', support),
]