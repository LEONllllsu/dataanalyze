# _*_ coding: utf-8 _*_
__author__ = 'leonsu'
__date__ = '2018/6/5 14:38'
from rest_framework import serializers
from users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return UserProfile.objects.create(**validated_data)
