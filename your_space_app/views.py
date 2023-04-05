from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Profile, FriendRequest, Friendship, Post, Comment, Like
from .serializers import (
    ProfileSerializer, FriendRequestSerializer, FriendshipSerializer,
    PostSerializer, CommentSerializer, LikeSerializer
)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        like = self.get_object()
        like.users.add(request.user)
        like.save()
        serializer = self.get_serializer(like)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        like = self.get_object()
        like.users.remove(request.user)
        like.save()
        serializer = self.get_serializer(like)
        return Response(serializer.data)
