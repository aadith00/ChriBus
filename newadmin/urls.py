from django.urls import path
from .views import index, dashboard, get_model_data, admin_login, admin_logout

urlpatterns = [

    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    # path('charts', bus_chart, name='bus-chart'),
    path('api/model-data/', get_model_data, name='get_model_data'),
    path('dashboard', admin_login, name='admin-login'),
    path('adlogout', admin_logout, name='admin-logout'),

]