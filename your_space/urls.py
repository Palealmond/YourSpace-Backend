from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from your_space_app.views import (
    ProfileViewSet, FriendRequestViewSet, FriendshipViewSet,
    PostViewSet, CommentViewSet, LikeViewSet
)

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'friend-requests', FriendRequestViewSet,
                basename='friend_request')
router.register(r'friendships', FriendshipViewSet, basename='friendship')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'likes', LikeViewSet, basename='like')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
]
