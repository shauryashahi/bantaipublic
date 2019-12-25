from rest_framework import routers
from api import views as myapp_views

router = routers.DefaultRouter()
router.register(r'users', myapp_views.UserViewset)
# router.register(r'friendships', myapp_views.FriendshipViewset)
