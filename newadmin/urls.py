from django.urls import path
from .views import dashboard

urlpatterns = [

    path('dashboard', dashboard, name='dashboard'),
    # path('charts', bus_chart, name='bus-chart'),


]