from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iso_links.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'iso_links.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<url>.*)/$', 'link.views.link'),
)
