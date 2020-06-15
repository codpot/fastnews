from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.news_list, {'category': 'news'}),
    url(r'^politics/$', views.news_list, {'category': 'politics'}),
    url(r'^economy/$', views.news_list, {'category': 'economy'}),
    url(r'^social/$', views.news_list, {'category': 'social'}),
    url(r'^life/$', views.news_list, {'category': 'life'}),
    url(r'^world/$', views.news_list, {'category': 'world'}),
    url(r'^it/$', views.news_list, {'category': 'it'}),
    url(r'^news/(?P<id>[0-9]+)$', views.news_detail),

    url(r'^debates/$', views.debates_list),
    url(r'^debates/(?P<id>[0-9]+)$', views.debates_detail),

    url(r'^notifications/$', views.notifications_list),
    url(r'^notifications/(?P<id>[0-9]+)$', views.notifications_detail),

    url(r'^likes/$', views.likes_list),
    url(r'^likes/(?P<id>[0-9]+)$', views.likes_detail),

    url(r'^write/$', views.write),

    url(r'^settlement/$', views.settlement_list),
    url(r'^settlement/(?P<id>[0-9]+)$', views.settlement_detail),

    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^myaccount/$', views.myaccount),
]
