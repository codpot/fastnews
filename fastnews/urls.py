from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.news_list, {'category': 'news'}, name='news_list'),
    url(r'^politics/$', views.news_list, {'category': 'politics'}, name='news_list_politics'),
    url(r'^economy/$', views.news_list, {'category': 'economy'}, name='news_list_economy'),
    url(r'^social/$', views.news_list, {'category': 'social'}, name='news_list_social'),
    url(r'^life/$', views.news_list, {'category': 'life'}, name='news_list_life'),
    url(r'^world/$', views.news_list, {'category': 'world'}, name='news_list_world'),
    url(r'^it/$', views.news_list, {'category': 'it'}, name='news_list_it'),
    url(r'^news/(?P<id>[0-9]+)$', views.news_detail, name='news_detail'),

    url(r'^search/$', views.search, name='search'),

    url(r'^debates/$', views.debates_list, name='debates_list'),
    url(r'^debates/recent/$', views.debates_list, name='debates_list_recent'),
    url(r'^debates/(?P<id>[0-9]+)$', views.debates_detail, name='debates_detail'),

    url(r'^notifications/$', views.notifications_list, name='notifications_list'),
    url(r'^likes/$', views.likes_list, name='likes_list'),
    url(r'^write/$', views.write, name='write'),

    url(r'^settlement/$', views.settlement_list, name='settlement_list'),
    url(r'^settlement/(?P<id>[0-9]+)$', views.settlement_detail, name='settlement_detail'),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^myaccount/$', views.myaccount, name='myaccount'),
]
