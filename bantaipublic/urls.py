from django.contrib import admin
from django.urls import path, include
from api.models import *
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/user/<user_id>/friendlist', FriendListViewSet.as_view()),
    path('api/user/<user_id>/suggestions', FriendSuggestionsViewSet.as_view())
]
