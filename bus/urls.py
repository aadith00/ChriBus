from django.urls import path
from .views import booking, search_buses, bus_details

urlpatterns = [

    path('booking/', booking),
    path('search', search_buses),
    # path('bus/<str:num_plate>/', bus_details, name='bus_details'),
    # path('book/<int:bus_id>/', book_ticket, name='book_ticket'),
    # path('search_results', search_bus),
]