from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from ueabc import views
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.home),
    url(r'^contacts/$', views.contacts),
    url(r'^members/$', views.general_page, { 'template_name' : 'members'}),
    
	url(r'^results/(\d{4}-\d{2})/$', views.results),
	url(r'^media/news/$', views.news),
	url(r'^media/videos/$', views.videos),
	url(r'^media\/photos\/(?P<photos>\w+)*\/$', views.photos),

	# if no match from above urls, this will find the page if its generic
	url(r'^(?P<template_name>\w+\/\w+(-\w+)*(\/\w+(-\w+)*)*)\/$', views.general_page),
)
