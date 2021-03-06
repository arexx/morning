from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'morning.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.index, name='index'),
    url(r'^forecast$', hello.views.forecast, name='forecast'),
    url(r'^mta$', hello.views.mta, name='mta'),
    url(r'^admin/', include(admin.site.urls)),


)
