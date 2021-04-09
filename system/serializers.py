# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework import viewsets
from django.contrib.auth.models import  User
#的发射点

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id",'url', 'username', 'email', 'is_staff']

