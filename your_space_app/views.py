from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Profile, FriendRequest, Friendship, Post, Comment, Like
from .serializers import (
    ProfileSerializer, FriendRequestSerializer, FriendshipSerializer,
    PostSerializer, CommentSerializer, LikeSerializer
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView


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


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        return Response({'token': token.key, 'username': request.data['username']})


class MyView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # Perform actions with authenticated user
        return Response({'message': f'Authenticated user: {user.username}'})
