from django.conf.urls import patterns, url
from portofolio import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^portofolio/(?P<exercise_name>[\w\-]+)/$', views.exercise, name='exercise'),
)
