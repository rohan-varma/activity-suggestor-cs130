"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^api/', include('placefindr.urls')),
    #url(r'^', include('placefindr.urls')),
    url(r'^', include('placefindr.urls')),
]

# '''Alternative way of doing this'''
# if settings.DEBUG == True:
#     from django.http import HttpResponse
#
#     with open('./static/index.html', 'r') as myfile:
#         main_page_html = myfile.read()
#
#     def index(request):
#         return HttpResponse(main_page_html)
#
#     urlpatterns += [
#         url(r'^$', index),
#     ]
