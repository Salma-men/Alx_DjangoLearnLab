from django.urls import path
from .views import home
from django.contrib.auth import views as auth_views
from . import views



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

]
