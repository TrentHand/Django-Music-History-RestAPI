from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import *

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = genremodels.Genre
        fields = ('name','url', 'id')