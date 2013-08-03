from django.conf.urls import patterns, include, url
from knowledge.views import knowledge_index
from gluukb.forms import QuestionForm
from gluukb.views import IndexView
from sugarlink.views import logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^$', IndexView.as_view(), name='knowledge_index'),
    url(r'^questions/$', 'knowledge.views.knowledge_list', name='knowledge_list', kwargs={'Form': QuestionForm}),

    url(r'^questions/(?P<category_slug>[a-z0-9-_]+)/$', 'knowledge.views.knowledge_list',
        name='knowledge_list_category', kwargs={'Form': QuestionForm}),
    url(r'^ask/$', 'knowledge.views.knowledge_ask', name='knowledge_ask', kwargs={'Form': QuestionForm}),
    url(r'^', include('knowledge.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^logout/$', logout , name='logout'),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)
