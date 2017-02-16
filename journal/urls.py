from django.conf.urls import url
from journal import views
urlpatterns = [
    url(r'^post_list/$', views.post_list),
    url(r'^post_detail/(?P<id>\d+)/$', views.post_detail),
    url(r'^post_new/$', views.post_new),

]