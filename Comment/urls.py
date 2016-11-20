from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^logowanie$', views.logowanie, name='logowanie'),
    url(r'^songs$', views.search_songs, name='search_songs'),
]
