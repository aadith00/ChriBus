from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='rentals'),
    path('upload',views.upload,name='upload'),
    path('support/',views.contact,name='support'),
]