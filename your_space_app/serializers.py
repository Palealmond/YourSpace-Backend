from rest_framework import serializers
from .models import Profile, FriendRequest, Friendship, Post, Comment, Like
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'


class FriendRequestSerializer(serializers.ModelSerializer):
    from_user = UserSerializer()
    to_user = UserSerializer()

    class Meta:
        model = FriendRequest
        fields = '__all__'


class FriendshipSerializer(serializers.ModelSerializer):
    user1 = UserSerializer()
    user2 = UserSerializer()

    class Meta:
        model = Friendship
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Like
        fields = '__all__'


# Add these helper functions to your serializers.py file:

def get_profile_serializer(*args, **kwargs):
    return ProfileSerializer(*args, **kwargs)

def get_friend_request_serializer(*args, **kwargs):
    return FriendRequestSerializer(*args, **kwargs)

def get_friendship_serializer(*args, **kwargs):
    return FriendshipSerializer(*args, **kwargs)

def get_post_serializer(*args, **kwargs):
    return PostSerializer(*args, **kwargs)

def get_comment_serializer(*args, **kwargs):
    return CommentSerializer(*args, **kwargs)

def get_like_serializer(*args, **kwargs):
    return LikeSerializer(*args, **kwargs)
