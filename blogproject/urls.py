from django.conf.urls import url
from django.contrib import admin

from blog.views import *
from comments.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', category, name='category'),
    
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', post_comment, name='post_comment'),

]