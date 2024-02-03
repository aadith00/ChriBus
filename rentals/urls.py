from django.urls import path
from .views import index, upload, contact
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

]
