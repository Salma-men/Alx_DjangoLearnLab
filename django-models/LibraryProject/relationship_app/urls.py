from django.urls import path
from . import views  # Import views to use views.register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Existing Routes for Books and Library Details
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication Routes
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),  # Use views.register here
]
