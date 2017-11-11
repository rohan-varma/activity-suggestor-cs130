from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/$', views.index, name='index'),
    url(r'^/api/suggest/', views.suggest, name='suggest'),
    url(r'^/api/share/(?P<mode>[a-zA-Z0-9_]+)/$', views.share, name='share')
]
