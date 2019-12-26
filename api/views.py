from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework import generics
from .serializers import *
from .models import *

class FriendListViewSet(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = get_object_or_404(User,user_id=self.kwargs['user_id'])
        return user.friends.all()

class FriendSuggestionsViewSet(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = get_object_or_404(User,user_id=self.kwargs['user_id'])
        suggestions = user.friend_of_friends()
        num_suggestions = len(suggestions)
        if num_suggestions < settings.MAX_NUM_SUGGESTIONS:
            random_suggestions = User.objects.exclude(
                user_id=self.kwargs['user_id']
            ).order_by('?')[:(settings.MAX_NUM_SUGGESTIONS-num_suggestions)]
            suggestions += random_suggestions
        return suggestions[:(settings.MAX_NUM_SUGGESTIONS)]
