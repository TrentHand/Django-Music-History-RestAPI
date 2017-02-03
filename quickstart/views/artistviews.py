from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import *
from quickstart.models import *

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Artists to be viewed or edited
    """
    queryset = artistmodels.Artist.objects.all()
    serializer_class = artistserializer.ArtistSerializer