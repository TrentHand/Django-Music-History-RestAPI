from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import *

class SongSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Artist mode. 
    fields include: 
                name(from model)
                album(from model)
                artist(from model)
                genre(from model)
                url
                id
    """
    class Meta:
        model = songmodels.Song
        fields = ('name', 'album', 'artist', 'genre','url', 'id')