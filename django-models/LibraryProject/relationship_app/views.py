from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-Based View for Listing Books
def list_books(request):
    books = Book.objects.all()  # Make sure this line exists
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View for Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Use full path
    context_object_name = 'library'
