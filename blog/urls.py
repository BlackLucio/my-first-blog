from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='listado'),
    url(r'^post_list_mayor$', views.post_list_mayor),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^procesadores$', views.post_list_procesadores),
    url(r'^procesadores_menor$', views.post_list_procesadores_menor),
    url(r'^placa_video$', views.post_list_placa_video),
    url(r'^placa_video_menor$', views.post_list_placa_video_menor),
    url(r'^otros$', views.post_list_otros),
]