from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Profile, FriendRequest, Friendship, Post, Comment, Like

admin.site.register(Profile)
admin.site.register(FriendRequest)
admin.site.register(Friendship)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
