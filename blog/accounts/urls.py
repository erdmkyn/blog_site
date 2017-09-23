from django.conf.urls import url
from .views import *
from django.contrib import admin
from .forms import LoginForm

app_name = 'accounts'

admin.autodiscover()
urlpatterns = [

        url(r'^login/$', login_view, name='login'),

        url(r'^logout/$', logout_view, name='logout'),

        url(r'^register/$', register_view, name='register'),


]
