from django.urls import path
from .views import sigin_home, user_register, user_login, user_logout


urlpatterns = [
    
    path('', user_register),
    path('register', user_register),
    path('login', user_login),
    path('home', sigin_home),
    path('logout', user_logout),

]