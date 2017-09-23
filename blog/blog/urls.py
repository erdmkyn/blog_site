"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import home_view
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404,handler500
from blog import views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home_view, name='home'),

    url(r'^post/', include('post.urls', namespace='post')),

    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    url('^api/v1/', include('social_django.urls', namespace='social')),

    url(r'^users/', include('users.urls', namespace='users'))



]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = views.error404
