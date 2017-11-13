from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^suggest/', views.suggest, name='suggest'),
    url(r'^share/(?P<mode>[a-zA-Z0-9_]+)/$', views.share, name='share')
]
