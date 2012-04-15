from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from activities.views import ActivitiesView, ActivityView
from contact.views import ContactView
from index.views import IndexView
from our_installations.views import OurInstallationsView
from partners.views import PartnersView
from social.views import SocialView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'atividades/$', ActivitiesView.as_view(), name='activities'),
    url(r'atividades/(?P<slug>[\w-]+)$$', ActivityView.as_view(), name='activity'),
    url(r'nossas-instalacoes/$', OurInstallationsView.as_view(), name='our_installations'),
    url(r'parceiros/$', PartnersView.as_view(), name='partners'),
    url(r'noticias/$', SocialView.as_view(), name='social'),
    url(r'contato/$', ContactView.as_view(), name='contact'),
    url(r'^/?$', IndexView.as_view(), name='index'),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)

urlpatterns += staticfiles_urlpatterns()
