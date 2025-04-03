from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            return Response({"message": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Liked successfully"}, status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        like = Like.objects.filter(user=request.user, post_id=pk).first()
        if like:
            like.delete()
            return Response({"message": "Unliked successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)
