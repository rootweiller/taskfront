from django.conf.urls import *

from .views import RegisterUser, RolAdd


urlpatterns = [
    url(r'^register/', RegisterUser.as_view(), name='RegisterUser'),
    url(r'^rol/add', RolAdd.as_view(), name='RolAdd')
]