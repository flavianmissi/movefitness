from django.conf.urls import patterns, include, url
from django.contrib import admin

from content.views import ContentView


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'move_fitness.views.home', name='home'),
    url(r'^(?P<slug>[\w-]+)?/$', ContentView.as_view(), name='content'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
