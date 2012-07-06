from django.conf.urls import patterns, include, url
from misquote.views import MasterView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

	# Project Views
	url(r'^$', MasterView.as_view(), name='Index')
	
	# Examples
	# New named templates
	# url(r'^alt/$', MarthaView.as_view(template_name="alt_index.html"), name='home-alt'),
)
