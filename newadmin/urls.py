from django.urls import path
from .views import dashboard, tables

urlpatterns = [

    path('dashboard', dashboard, name='dashboard'),
    path('datatables', tables, name='table'),

]