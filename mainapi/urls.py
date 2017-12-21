from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers


urlpatterns = [
    url(r'^pets/$', views.PetList.as_view()),
    url(r'^pets/(?P<pk>[0-9]+)/$', views.PetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]