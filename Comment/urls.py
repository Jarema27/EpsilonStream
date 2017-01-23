from django.conf.urls import url
from . import views
from django.views.generic.edit import CreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^logowanie/$', views.user_login, name='logowanie'),
    url(r'^songs/$', views.search_songs, name='search_songs'),
    url(r'^utwor/$', views.utwor, name='utwor'),
    url(r'^dodaj/(?P<pk>[0-9]+)/$', views.dodaj, name='dodaj'),
    url(r'^lista/$', views.nowa_lista_ba, name='nowa_lista_ba'),
    url(r'^nowa_lista/(?P<sid>[0-9]+)/$', views.nowa_lista, name='nowa_lista'),
    url(r'^dodaj/(?P<lid>[0-9]+)/song/(?P<sid>[0-9]+)/$', views.dodaj_do_listy, name='dodaj_do_listy'),
    url(r'^utwor/(?P<pk>[0-9]+)/$', views.utwor, name='utwor'),
    url(r'^playlist/(?P<pk>[0-9]+)/song/(?P<sid>[0-9]+)/$', views.playList, name='playList'),
    url(r'^edit/(?P<pk>[0-9]+)/', views.edit, name='edit'),
    url(r'^remove/$', views.remove, name='remove'),
    url(r'^remove/list/(?P<pk>[0-9]+)/song/$', views.remove_song, name='remove_song'),
    url(r'^listyod/$', views.listy, name='listyOd'),
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^logout/$', views.user_logout, name='logout'),
]
