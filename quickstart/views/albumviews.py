from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import *
from quickstart.models import *

class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Albums to be viewed or edited
    """
    queryset = albummodels.Album.objects.all()
    serializer_class = albumserializer.AlbumSerializer