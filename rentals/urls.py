from django.urls import path
from .views import index, upload, contact,register

urlpatterns = [
    path('',index),
    path('upload',upload),
    path('support/',contact),
    path('login',register)
]