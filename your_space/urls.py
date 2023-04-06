from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from your_space_app.views import (
    ProfileViewSet, FriendRequestViewSet, FriendshipViewSet,
    PostViewSet, CommentViewSet, LikeViewSet, MyView, CustomAuthToken, UserCreateView
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
    path('api/login/', CustomAuthToken.as_view(),  name='create-token'),
    path('api/verify/', MyView.as_view(), name='my-view'),
    path('', include(router.urls)),
    path('create-user/', UserCreateView.as_view(), name='create-user'),

]
