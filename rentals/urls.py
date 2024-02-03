from django.urls import path
from .views import index, upload, contact
from base.views import home,user_login
from bus.views import booking

urlpatterns = [
    path('', index, name='index'),
    path('upload', upload, name='upload'),
    path('support/', contact, name='contact'),
    path('home', home),
    path('booking',booking),
    path('login',user_login)

]
