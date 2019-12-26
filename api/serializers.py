from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id','user_id', 'username', 'dob','name','gender','location','pic_url')

class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friendship
        fields = ('id', 'profile_1', 'profile_2', 'created_at')
