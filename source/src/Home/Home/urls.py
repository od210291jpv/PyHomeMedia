"""Home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG, MEDIA_URL
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^playlist/(?P<plid>\d+)/view/$', 'Home.Application.views.show_playlist', name='show_playlist'),
    url(r'^playlists/$', 'Home.Application.views.playlists', name='playlist'),
    url(r'^$', 'Home.Application.views.index', name='index'),
    url(r'^home/$', 'Home.Application.views.home', name='home'),
    url(r'^test/$', 'Home.Application.views.test', name='test')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
