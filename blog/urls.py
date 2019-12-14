from django.conf.urls import url 
import os
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^Tag/(?P<pk>[0-9]+)/$', views.TagView, name='Tag'),
    url(r'^uploadfile$', views.upload, name='upload'),
    url(r'^Editor/$', views.Editor, name='Editor'),
]

media_root = os.path.join(settings.BASE_DIR,'upload')
urlpatterns += static('/upload/', document_root=media_root)
