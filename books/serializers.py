from django.contrib.auth.models import User
from rest_framework import serializers
from books.models import Bookshelf


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookshelf
        exclude = 'url'
