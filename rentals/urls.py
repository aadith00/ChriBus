from django.urls import path
from .views import index, upload, contact, bullet, toyota ,bikerental,rent_details
from base.views import home,user_login,rentals
from bus.views import booking

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload, name='upload'),
    path('support/', contact, name='contact'),
    path('home', home, name='home'),
    path('booking',booking, name='booking'),
    path('login',user_login, name='user-login'),
    path('rentals', rentals, name='rentals'),
    path('bikerental',bikerental,name='bikerental'),
     path('rent-details',rent_details,name='rent-details'), 
    path('bullet',bullet,name='bullet'),
    path('toyota',toyota,name='toyota'),
]
