from django.urls import path,include
from .views import rentals,support

urlpatterns = [
    path('rentals', rentals),
    path('support', support),
]