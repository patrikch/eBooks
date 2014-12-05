from django.conf.urls import patterns, include, url
import os
from django.contrib.auth import logout
#from django.contrib import admin

site_media = os.path.join(os.path.dirname(__file__),
    "site_media")

urlpatterns = patterns('',    
    #session management
    url(r"^login/$","django.contrib.auth.views.login",name="login"),
    url(r"^logout/$",'django.contrib.auth.views.logout',name="logout"),                       
    # books app
    url(r'^$', 'books.views.home', name='home'),
    url(r'^home/$', 'books.views.home', name='home'),
    url(r'^detail/(\d+)/$', 'books.views.detail', name='detail'),
    url(r'^search/$', 'books.views.search', name='search'),
    url(r'^keysearch/$', 'books.views.keysearch', name='keysearch'),
    url(r'^list/$', 'books.views.list', name='list'),
    #site media
    url(r"^site_media/(?P<path>.*)$","django.views.static.serve",
         {"document_root":site_media}),
)
