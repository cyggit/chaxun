from django.conf.urls import patterns, include, url
from django.contrib import admin
from chaxun1.views import index,test

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chaxun.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^test/$',test)
)
