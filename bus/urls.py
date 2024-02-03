from django.urls import path
from .views import booking, search_buses, bus_details
from base.views import home

urlpatterns = [

    path('booking/', booking),
    path('search', search_buses, name='search-buses'),
    path('bus/<str:num_plate>/', bus_details, name='bus_details'),
    path('home', home),
    # path('book/<int:bus_id>/', book_ticket, name='book_ticket'),
    # path('search_results', search_bus)
]