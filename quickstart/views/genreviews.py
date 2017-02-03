from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import *
from quickstart.models import *

class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Genres to be viewed or edited
    """
    queryset = genremodels.Genre.objects.all()
    serializer_class = genreserializer.GenreSerializer