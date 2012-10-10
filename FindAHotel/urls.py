# -*- coding: utf-8 -*- 
# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from frontend.views import index
from django.contrib import admin
from django.http import HttpResponseRedirect
admin.autodiscover()


urlpatterns = patterns('',
    (r'^$', lambda r : HttpResponseRedirect('find/')),
    (r'^find/$', index),
    # Examples:
    # url(r'^$', 'FindAHotel.views.home', name='home'),
    # url(r'^FindAHotel/', include('FindAHotel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'^admin/', include(admin.site.urls)),
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/django/list/static'}),

)
