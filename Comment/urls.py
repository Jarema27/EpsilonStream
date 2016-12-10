from django.conf.urls import url
from . import views
from django.views.generic.edit import CreateView

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^logowanie$', views.logowanie, name='logowanie'),
    url(r'^songs$', views.search_songs, name='search_songs'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^registration_complete/$', views.registration_complete,
 	name='Registration_Complete'),
]
