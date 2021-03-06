"""velepsi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from places.views import index,detail ,new_place , new_media,new_review,like_place
from profiles.views import register, login, logout
from activities.views import activity,new_activity ,like_activity,activity_new_review,activity_new_media,activity_detail,activity_comment



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name="index"),
    url(r'^register$',register,name="register"),
    url(r'^login$',login,name="login"),
    url(r'^logout$',logout,name="logout"),

    url(r'^places/(?P<id>\d+)$', detail, name='place_detail'),
    url(r'^places/(?P<place_id>\d+)/new-media$', new_media, name='new_media'),
    url(r'^places/(?P<place_id>\d+)/new-review$', new_review, name='new_review'),
    url(r'^places/(?P<place_id>\d+)/like$', like_place, name='like_place'),
    url(r'^new-place$', new_place, name="new_place"),

    url(r'^activity',activity,name="activity"),
    url(r'^new_activity$', new_activity, name="new_activity"),
    url(r'^activities/(?P<activity_id>\d+)/activity_new_media$', activity_new_media, name='activity_new_media'),
    url(r'^activities/(?P<activity_id>\d+)/activity_new_review$', activity_new_review, name='activity_new_review'),
    url(r'^activities/(?P<activity_id>\d+)/like$', like_activity, name='like_activity'),
    url(r'^activities/(?P<id>[0-9]+)/$', activity_detail, name='activity_detail'),

    url(r'^comments/(?P<id>[0-9]+)/$', activity_comment, name='comments'),

    url(r"^api/", include("places.urls")),
    url(r"^api/", include("activities.urls")),
    url(r"^api/", include("profiles.urls")),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve , {
            "document_root" :settings.MEDIA_ROOT,
        }),
    ]

