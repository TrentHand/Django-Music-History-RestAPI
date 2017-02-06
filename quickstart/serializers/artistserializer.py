from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import *

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Artist mode. 
    fields include: name(from model)
                genre(from model)
                url
                id
    """
    class Meta:
        model = artistmodels.Artist
        fields = ('name', 'genre', 'url', 'id')