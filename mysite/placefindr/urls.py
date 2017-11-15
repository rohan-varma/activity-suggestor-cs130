from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/suggest/', views.suggest, name='suggest'),
    url(r'^api/share/(?P<sharing_method>[a-zA-Z0-9_]+)/$', views.share, name='share'),
    url(r'^$', views.index, name='index'), #TODO
]
