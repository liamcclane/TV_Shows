from django.conf.urls import url
from . import views

print('we are inside the urls function inside dashboard')

urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^shows/createPg$', views.createPg),
    url(r'^shows/createShow$', views.createShow),
    url(r'^shows/(?P<show_id>\d+)$', views.showDetails),
    url(r'^shows/(?P<show_id>\d+)/delete', views.deleteShow),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.editShow),
    url(r'^shows/(?P<show_id>\d+)/updateShow$', views.updateShow),
]