from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import login
from accounts import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', login, name='login', kwargs={'template_name':'accounts/login_form.html'}),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', logout, name='logout', kwargs={
        'next_page': settings.LOGIN_URL,}),


]