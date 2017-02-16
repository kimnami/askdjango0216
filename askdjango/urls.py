"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.shortcuts import redirect

# def root(request):
#     return redirect('post_list')

urlpatterns = [
    url(r'^$', lambda request: redirect('blog:post_list')),
    url(r'^accounts/$', include('accounts.urls')), #accounts app내에서는 auth app과 마찬가지로 namespace를 걸지 않음.
    url(r'^admin/', admin.site.urls),
    url(r'blog/', include('blog.urls', namespace='blog')),
    url(r'journal/', include('journal.urls', namespace='journal')),

    url(r'^webtoon/', include('webtoon.urls', namespace='webtoon'), name="webtoon"),
#webtoon뒤에 주소가 더 필요하기 때문에 정규표현식을 마무리짓는 $를 써주지 않는다!

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)), ]