from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from activities.views import ActivitiesView
from our_installations.views import OurInstallationsView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'atividades?/$', ActivitiesView.as_view(), name='activities'),
    url(r'nossas-instalacoes?/$', OurInstallationsView.as_view(), name='our_installations'),
)

urlpatterns += staticfiles_urlpatterns()
