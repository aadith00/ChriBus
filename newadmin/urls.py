from django.urls import path
from .views import index, dashboard, get_model_data

urlpatterns = [

    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    # path('charts', bus_chart, name='bus-chart'),
    path('api/model-data/', get_model_data, name='get_model_data'),


]