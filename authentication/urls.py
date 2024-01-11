from django.contrib import admin
from django.urls import path, include
from .views import admin_login

urlpatterns = [
    path('' , admin_login)
]