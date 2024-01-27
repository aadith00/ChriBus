from django.urls import path
from .views import booking, search_buses

urlpatterns = [

    path('booking', booking),
    path('search', search_buses, name='search_buses'),
    
]