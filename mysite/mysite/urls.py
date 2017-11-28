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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('placefindr.urls')),
]

if settings.DEBUG == True:

    with open(os.path.join(settings.STATIC_ROOT, 'splash.html'), 'r') as myfile:
        splash_page_html = myfile.read()
    with open(os.path.join(settings.STATIC_ROOT, 'index.html'), 'r') as myfile:
        main_page_html = myfile.read()

    from django.http import HttpResponse
    def splash_page_view(request):
        return HttpResponse(splash_page_html)
    def main_page_view(request):
        return HttpResponse(main_page_html)

    from django.views.generic.base import RedirectView
    from django.views import static

    urlpatterns += [
        # home, splash & main page urls
        url(r'^$', RedirectView.as_view(pattern_name='splash-page', permanent=False), name="home-path"),
        url(r'^splash$', splash_page_view, name="splash-page"),
        url(r'^main$', main_page_view, name="main-page"),

        # generic /static urls
        url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT,}),
    ]
