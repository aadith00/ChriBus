from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='rentals'),
    path('',views.contact,name='support') 
]