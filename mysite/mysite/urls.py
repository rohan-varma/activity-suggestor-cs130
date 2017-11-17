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

import os
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('placefindr.urls')),
]

if settings.DEBUG == True:
    # This adds URLs for static files
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT,}),
        #url(r'^uploads/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT,}),
    ]

if settings.DEBUG == True:
    # This adds URL for main page (splash.html)

    with open(os.path.join(settings.STATIC_ROOT, 'splash.html'), 'r') as myfile:
        main_page_html = myfile.read()

    from django.http import HttpResponse
    def main_page_view(request):
        return HttpResponse(main_page_html)

    urlpatterns += [
        url(r'^', main_page_view),
    ]
