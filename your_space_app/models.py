from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def default_profile_image():
    return "./img/image.png"


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(
        upload_to='profile_images', blank=True, default=default_profile_image)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        User, related_name='friend_requests_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='friend_requests_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Friendship(models.Model):
    user1 = models.ForeignKey(
        User, related_name='friendships1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(
        User, related_name='friendships2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# class Comment(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="comment")
#     post = models.ForeignKey(
#         Post, on_delete=models.CASCADE, related_name="comment")
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
