from django.urls import path
from .views import booking, search_buses, bus_details, book_ticket
from base.views import home, user_login, user_logout
from rentals.views import upload

urlpatterns = [

    path('booking/', booking),
    path('search', search_buses, name='search-buses'),
    path('home', home),
    path('upload', upload, name='upload'),
    path('register',user_login, name='user_login'),
    path('bus/book/<str:num_plate>/<str:tick_num>/<str:depar_date>/', book_ticket, name='book-ticket'),
    path('bus/<str:num_plate>/', bus_details, name='bus_details'),
    path('logout', user_logout, name='logout'),

    # path('search_results', search_bus)
]