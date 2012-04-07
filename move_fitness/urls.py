from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from content.views import ContentView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<slug>[\w-]+)?/$', ContentView.as_view(), name='content'),
)

urlpatterns += staticfiles_urlpatterns()
