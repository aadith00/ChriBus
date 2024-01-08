from django.urls import path
from .views import rentals

urlpatterns = [
    path('rentals', rentals),
]