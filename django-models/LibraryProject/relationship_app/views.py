from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book   # Ensure Library is imported

# Function-Based View for Listing Books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View for Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
