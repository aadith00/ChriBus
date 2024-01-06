from django.urls import path
from .views import signup,booking


urlpatterns = [
    path('', booking),
    path('booking', booking),
    path('signup', signup),
]