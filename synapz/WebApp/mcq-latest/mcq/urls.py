from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

from mcqportal import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	 url(r'^$', views.index, name='index'),
	  # Login / logout.
#    (r'^login/$', 'django.contrib.auth.views.login'),
#    (r'^logout/$', logout_page),

    # Examples:
    # url(r'^$', 'mcq.views.home', name='home'),
    # url(r'^mcq/', include('mcq.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^mcqportal/', include('mcqportal.urls', namespace="mcqportal")),

  # Serve static content.
 #   (r'^static/(?P<path>.*)$', 'django.views.static.serve',
  #      {'document_root': 'static'}),

)
