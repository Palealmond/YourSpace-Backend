"""
URL configuration for your_space project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from your_space_app import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('profiles/', views.profile_list),
    path('profiles/<int:pk>/', views.profile_detail),
    path('profiles/create/', views.profile_list),
    path('profiles/<int:pk>/update/', views.profile_detail),
    path('profiles/<int:pk>/delete/', views.profile_detail),

    path('friend-requests/', views.friend_request_list),
    path('friend-requests/<int:pk>/', views.friend_request_detail),
    path('friend-requests/create/', views.friend_request_list),
    path('friend-requests/<int:pk>/delete/', views.friend_request_detail),

    path('friendships/', views.friendship_list),
    path('friendships/<int:pk>/', views.friendship_detail),
    path('friendships/create/', views.friendship_list),
    path('friendships/<int:pk>/delete/', views.friendship_detail),

    path('posts/', views.post_list),
    path('posts/<int:pk>/', views.post_detail),
    path('posts/create/', views.post_list),
    path('posts/<int:pk>/update/', views.post_detail),
    path('posts/<int:pk>/delete/', views.post_detail),

    path('comments/', views.comment_list),
    path('comments/<int:pk>/', views.comment_detail),
    path('comments/create/', views.comment_list),
    path('comments/<int:pk>/update/', views.comment_detail),
    path('comments/<int:pk>/delete/', views.comment_detail),

    path('likes/', views.like_list),
    path('likes/<int:pk>/', views.like_detail),
    path('likes/create/', views.like_list),
    path('likes/<int:pk>/delete/', views.like_detail),



]
