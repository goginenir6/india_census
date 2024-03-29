"""Gramenertestcase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from usecasenas.views import index, home, logout, india_census, mobile_penetration, similar_districts

urlpatterns = [
    url(r'^$',index),
    url(r'^home$',home),
    url('', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^india_census/$', india_census, name='india_census'),
    url(r'^mobile_penetration/$', mobile_penetration, name='mobile_penetration'),
    url(r'^similar_districts/$', similar_districts, name='similar_districts'),
    url(r'^logout/$', logout),
]