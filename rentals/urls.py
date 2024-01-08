from django.urls import path
from .views import rentals,support

urlpatterns = [
    path('rentals', rentals),
    path('support', support),
]