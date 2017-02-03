from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import *
from quickstart.models import *

class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Songs to be viewed or edited
    """
    queryset = songmodels.Song.objects.all()
    serializer_class = songserializer.SongSerializer