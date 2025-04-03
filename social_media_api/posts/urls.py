from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import UserFeedView
from .views import LikePostView, UnlikePostView




router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-comments'),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
