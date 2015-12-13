from django.conf.urls import patterns, url
from portofolionew import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
)  # New!)
