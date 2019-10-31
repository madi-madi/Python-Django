from django.conf.urls import url
from django.urls import path

from . import views
app_name = 'Post'

urlpatterns = [
    # url('', views.index, name='index'),
    url(r'^$', views.getAll, name='posts'),
    url(r'^(?P<id>\d+)$', views.getById, name='post'),
    url(r'^create$', views.create_post, name='create_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post, name='edit_post'),



]
