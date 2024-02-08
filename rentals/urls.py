from django.urls import path
from .views import index, upload, contact, bullet, toyota ,bikerental,rent_details,submit_form,contact_form
from base.views import home, user_login, rentals, user_logout
from bus.views import booking

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload, name='upload'),
    path('support/', contact, name='contact'),
    path('home', home, name='home'),
    path('booking', booking, name='booking'),
    path('login',user_login, name='user-login'),
    path('rentals', rentals, name='rentals'),
    path('bikerental',bikerental,name='bikerental'),
     path('rent-details',rent_details,name='rent-details'), 
    path('bullet',bullet,name='bullet'),
    path('toyota',toyota,name='toyota'),
    path('submit_form', submit_form, name='submit_form'),
    path('contact/', contact_form, name='contact_form'),
    path('logout', user_logout, name='logout')
    # path('succesuss_page',success_page,name='success_page'),
]
