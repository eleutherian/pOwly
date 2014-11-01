from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pOwly.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('tutorial.urls')),
    #url(r'^tutorial/', include('tutorial.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
