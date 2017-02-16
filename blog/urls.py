from django.conf.urls import url
from blog import views
from blog import views_cbv


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post_form/$', views_cbv.blog_new, name='blog_new'),
    url(r'^(?P<id>\d+)/$', views.post_detail ,name='post_detail'),
]