from django.contrib.auth import *
from django.conf.urls import url

from . import views

app_name = 'core'

urlpatterns = [
    #url(r'^$', views.loginUser, name='loginUser'),
    url(r'^base/$', views.home, name='home'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    
]