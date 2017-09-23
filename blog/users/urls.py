from django.conf.urls import url
from .views import edit_profile, user_screen
from django.contrib import admin

app_name = 'users'
admin.autodiscover()
urlpatterns = [

        url(r'^(?P<username>.+)/screen_user/$', view=user_screen, name='user_screen'),
        url(r'^(?P<username>.+)/update/$',view=edit_profile , name='edit_profile')
]
