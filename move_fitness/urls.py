from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from activities.views import ActivitiesView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'atividades?/$', ActivitiesView.as_view(), name='activities'),
)

urlpatterns += staticfiles_urlpatterns()
