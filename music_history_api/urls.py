"""music_history_api URL Configuration

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
from django.conf.urls import url, include
from rest_framework import routers
from quickstart.views import *

router = routers.DefaultRouter()
router.register(r'users', userviews.UserViewSet)
router.register(r'groups', userviews.GroupViewSet)
router.register(r'songs', songviews.SongViewSet)
router.register(r'albums', albumviews.AlbumViewSet)
router.register(r'artists', artistviews.ArtistViewSet)
router.register(r'genres', genreviews.GenreViewSet)

#Wire up our API using automatic URL routing
#Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
