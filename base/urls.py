from django.urls import path
from .views import home,booking


urlpatterns = [
    path('', home),
    path('home', home),
    path('booking', booking),
    
]