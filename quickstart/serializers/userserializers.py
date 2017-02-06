from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Artist mode. 
    fields include: 
                username(from model)
                email(from model)
                url
                id
    """
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'id')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Artist mode. 
    fields include: 
                name(from model)
                url
                id
    """
    class Meta:
        model = Group
        fields = ('url', 'name','id')