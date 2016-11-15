from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post, name="link"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_full, name="link2"),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA)
