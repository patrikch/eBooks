from django.conf.urls import patterns, include, url
import os
#from django.contrib import admin

site_media = os.path.join(os.path.dirname(__file__),
    "site_media")

urlpatterns = patterns('',    
    #session management
    url(r"^login/$","django.contrib.auth.views.login",name="login"),
    url(r"^logout/$",logout_page,name="logout"),
    # books app
    url(r'^home$', 'eBooksWeb.views.home', name='home'),
    url(r'^detail/(\d+)/$', 'eBooksWeb.views.detail', name='detail'),
    url(r'^search$', 'eBooksWeb.views.search', name='search'),
    url(r'^keysearch$', 'eBooksWeb.views.keysearch', name='keysearch'),                       
    #site media
    url(r"^site_media/(?P<path>.*)$","django.views.static.serve",
         {"document_root":site_media}),
)
