from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import *

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = songmodels.Song
        fields = ('name', 'album', 'artist', 'genre','url', 'id')