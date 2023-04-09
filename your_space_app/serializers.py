from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, FriendRequest, Friendship, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = '__all__'


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ('id', 'from_user', 'to_user', 'created_at')


class FriendshipSerializer(serializers.ModelSerializer):
    user1 = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user1.username')
    user2 = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user2.username')

    class Meta:
        model = Friendship
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at',
                  'updated_at', 'subject', 'category', 'user']
        read_only_fields = ['created_at', 'updated_at']

# class CommentSerializer(serializers.ModelSerializer):
#     user = UserSerializer(source='user_id', read_only=True)

#     class Meta:
#         model = Comment
#         fields = ('id', 'user', 'post', 'content', 'created_at')


# class LikeSerializer(serializers.ModelSerializer):
#     user = UserSerializer(source='user_id', read_only=True)

#     class Meta:
#         model = Like
#         fields = ('id', 'user', 'post', 'created_at')
