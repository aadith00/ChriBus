from django.urls import path
from .views import index, upload, contact

urlpatterns = [
    path('',index),
    path('upload/',upload),
    path('support/',contact),
]