from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import *

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = artistmodels.Artist
        fields = ('name', 'genre', 'url', 'id')