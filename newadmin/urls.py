from django.urls import path
from .views import dashboard, tables, bus_chart

urlpatterns = [

    path('dashboard', dashboard, name='dashboard'),
    path('datatables', tables, name='table'),
    path('bus-chart', bus_chart, name='bus-chart'),

]