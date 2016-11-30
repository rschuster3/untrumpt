"""untrumpt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

import views as base_views
from organizations import views as organizations_views


urlpatterns = [
    url(r'^$', base_views.index, name='home'),
    url(r'^organizations/$', organizations_views.organization_list, name='organization_list'),
    url(r'^twitter-feed/$', base_views.twitter_feed, name='twitter_feed'),
    url(r'^admin/', admin.site.urls),
]
