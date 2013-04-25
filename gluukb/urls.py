from django.conf.urls import patterns, include, url
from knowledge.views import knowledge_index

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', knowledge_index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^knowledge/', include('knowledge.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
)
