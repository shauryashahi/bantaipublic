from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from .serializers import *
from .models import *
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

def friend_list(request, user_id):
    user = get_object_or_404(User,user_id=user_id)
    friends = user.friends.all()
    return HttpResponse(friends, content_type='application/json')

def friend_suggestions(request,user_id):
    user = get_object_or_404(User,user_id=user_id)
    friend_ids = user.friends.all().values_list('id', flat=True)
    friend_of_friends_ids = Friendship.objects.filter(profile_1_id__in=friend_ids).values_list('profile_2_id', flat=True)
    friend_of_friends = User.objects.filter(id__in=friend_of_friends_ids)
    return HttpResponse(friend_of_friends, content_type='application/json')
