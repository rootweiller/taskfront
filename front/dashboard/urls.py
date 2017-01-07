from django.conf.urls import *
from django.contrib import admin


from .views import Login, Dashboard, Logout

urlpatterns = [


    url(r'^$', Login.as_view(), name='Login'),

    url(r'^dashboard/', Dashboard.as_view(), name='Dashboard'),

    url(r'^logout/', Logout.as_view(), name='Logout'),
]
