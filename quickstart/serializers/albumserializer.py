from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import *

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Artist mode. 
    fields include: 
                name(from model)
                artist(from model)
                genre(from model)
                url
                id
    """
    class Meta:
        model = albummodels.Album
        fields = ('name', 'artist', 'genre', 'id', 'url')