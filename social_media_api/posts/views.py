from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from notifications.models import Notification
from rest_framework.generics import get_object_or_404  # ✅ Use generics.get_object_or_404

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # ✅ Fix: Using generics.get_object_or_404
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            return Response({"message": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Create a notification when a post is liked
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )

        return Response({"message": "Liked successfully"}, status=status.HTTP_201_CREATED)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # ✅ Fix: Using generics.get_object_or_404
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"message": "Unliked successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"message": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)


