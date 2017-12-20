from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers


urlpatterns = [
url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='login_then_login'),
url(r'^pet-list/$', views.pet_list, name='status_list'),
url(r'^pet-user/$', views.pet_user, name='status_list'),
]