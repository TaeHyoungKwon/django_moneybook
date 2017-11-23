from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^create/$', views.moneybook_create,name='moneybook_create'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail,name='detail'),
]
