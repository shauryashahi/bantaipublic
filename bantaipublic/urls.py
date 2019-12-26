from django.contrib import admin
from django.urls import path, include
from api.models import *
from rest_framework import routers
from api.views import *


router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/friendships', FriendshipViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/user/<user_id>/friendlist', friend_list),
    path('api/user/<user_id>/suggestions', friend_suggestions)
]
