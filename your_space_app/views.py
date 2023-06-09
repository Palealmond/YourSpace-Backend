from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from .models import Profile, FriendRequest, Friendship, Post, User
from .serializers import (
    ProfileSerializer, FriendRequestSerializer, FriendshipSerializer,
    PostSerializer,  UserSerializer,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView


class ProfileByUsernameAPIView(APIView):
    def get(self, request, username):
        profile = get_object_or_404(Profile, user__username=username)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Manually set the user_id field to the ID of the user making the request
        serializer.validated_data['user_id'] = request.user.id

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class FriendRequestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Manually set the user_id field to the ID of the user making the request
        serializer.validated_data['user_id'] = request.user.id

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class FriendshipViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Manually set the user_id field to the ID of the user making the request
        serializer.validated_data['user_id'] = request.user.id

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Manually set the user_id field to the ID of the user making the request
        serializer.validated_data['user_id'] = request.user.id

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# class LikeViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer

#     @action(detail=True, methods=['post'])
#     def like(self, request, pk=None):
#         like = self.get_object()
#         like.users.add(request.user)
#         like.save()
#         serializer = self.get_serializer(like)
#         return Response(serializer.data)

#     @action(detail=True, methods=['post'])
#     def unlike(self, request, pk=None):
#         like = self.get_object()
#         like.users.remove(request.user)
#         like.save()
#         serializer = self.get_serializer(like)
#         return Response(serializer.data)


class UserCreateView(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'id': user.id, 'username': user.username, 'token': token.key}, status=status.HTTP_200_OK)


class MyView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # Perform actions with authenticated user
        return Response({'message': f'Authenticated user: {user.username}'})
