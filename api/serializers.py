from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username')

# class FriendshipSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Friendship
#         fields = ('id', 'sender', 'receiver', 'created_at')
