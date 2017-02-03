from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import *

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = albummodels.Album
        fields = ('name', 'artist', 'genre', 'id', 'url')