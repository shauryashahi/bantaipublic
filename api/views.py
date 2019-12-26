from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from .serializers import *
from .models import *
from django.http import HttpResponse
from .utils import override_view_attributes

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        override_view_attributes(self)

class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        override_view_attributes(self)

def friend_list(request, user_id):
    user = get_object_or_404(User,user_id=user_id)
    friends = user.friends.all()
    return HttpResponse(friends, content_type='application/json')

def friend_suggestions(request,user_id):
    user = get_object_or_404(User,user_id=user_id)
    friend_of_friends = user.friend_of_friends
    return HttpResponse(friend_of_friends, content_type='application/json')
