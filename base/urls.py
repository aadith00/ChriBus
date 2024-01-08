from django.urls import path
from .views import signup,booking


urlpatterns = [
    path('', booking),
    path('bookings.html', booking),
    path('signup', signup),
]