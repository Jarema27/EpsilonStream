from django.conf.urls import url
from . import views
from django.views.generic.edit import CreateView

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^logowanie$', views.user_login, name='logowanie'),
    url(r'^songs$', views.search_songs, name='search_songs'),
    url(r'^utwor$', views.utwor, name='utwor'),
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^logout/$', views.user_logout, name='logout'),
]
