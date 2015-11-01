"""smart_bin URL Configuration

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
from bins.views import *
from registration.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index', 'smart_bin.views.home'),
    url(r'^bins', 'bins.views.bins'),
    url(r'^details', 'bins.views.details'), 
    url(r'^optimal-route', 'bins.views.optimalRoute'),
    url(r'^analytics', 'bins.views.analytics'), 
    url(r'^hello/$',hello),
    url(r'^$',myLogin),
    url(r'^login/$',myLogin),
    url(r'^account/login/',myLogin),
    url(r'^account/logout',logoutview),
    url(r'^master_data/','bins.views.my_json_view'),
    url(r'^date_wise_update/','bins.views.my_json_view2'),
    url(r'^generate_csv/','bins.views.get_csv'),
]
