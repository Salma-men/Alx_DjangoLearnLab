from django.urls import path
from .views import home
from django.contrib.auth import views as auth_views
from . import views
from .views import add_comment, edit_comment, delete_comment
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import search_posts
from taggit.views import TaggedItemView
from .models import Post




urlpatterns = [
    path('', home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Django’s built-in login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Django’s built-in logout view
    path('profile/', views.profile, name='profile'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # Update post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/comment/new/', add_comment, name='add-comment'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit-comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete-comment'),
    path('post/<int:post_id>/comment/new/', CommentCreateView.as_view(), name='add-comment'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'), 
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('search/', search_posts, name='search'),
    path('tags/<slug:tag_slug>/', TaggedItemView.as_view(model=Post), name='tagged-posts'),
]
