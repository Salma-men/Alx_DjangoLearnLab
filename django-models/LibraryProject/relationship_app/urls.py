from django.urls import path
from .views import list_books, LibraryDetailView, user_login, user_logout, register
from django.contrib.auth.views import LoginView, LogoutView  # Import built-in LoginView and LogoutView

urlpatterns = [
    # Existing Routes for Books and Library Details
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # New Authentication Routes
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
]
