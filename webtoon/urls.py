from django.conf.urls import url
from webtoon import views

urlpatterns = [
    url(r'^$', views.webtoon_list,),
    url(r'^search/$', views.get_title,),
    url(r'^counter/$', views.counter, name='counter'),
    url(r'^(django.conf.urls?P<id>\d+)/$', views.webtoon_detail),
    ]