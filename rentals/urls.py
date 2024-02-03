from django.urls import path
from .views import index, upload, contact, register
from base.views import home

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload, name='upload'),
    path('contact/', contact, name='contact'),
    path('home', home),
]
