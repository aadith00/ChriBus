from django.urls import path
from .views import user_register, user_login, user_logout, home, rentals
from bus.views import booking
from rentals.views import contact


urlpatterns = [

    path('', home, name='home'),
    # path('', user_register,name='user-reg'),
    path('register', user_register, name='user-registration'),
    path('login', user_login, name="login-user"),
    path('home', home, name='home'),
    path('logout', user_logout, name='user-logout'),
    path('booking', booking),
    path('support', contact),
    path('rentals', rentals)

]