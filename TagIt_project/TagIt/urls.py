from django.conf.urls import patterns, url
from TagIt import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^link/(?P<urlid>\d+)/$', views.url, name='url'),
        url(r'^tag/(?P<tagid>\d+)/$', views.tag, name='tag'),
        url(r'^urls/$', views.urls, name='urls'),
        )
