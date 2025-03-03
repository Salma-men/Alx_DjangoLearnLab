from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, Author 
from django.views.generic.detail import DetailView
from .models import Library, Book   
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test, permission_required


# Function-Based View for Listing Books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View for Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# User Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')  # Redirect to book list after login
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in user after registration
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Helper functions to check the user roles
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# View to add a new book (with permission check)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = get_object_or_404(Author, id=request.POST.get('author_id'))
        book = Book.objects.create(title=title, author=author)
        return redirect('book_list')
    return render(request, 'add_book.html')

# View to edit an existing book (with permission check)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = get_object_or_404(Author, id=request.POST.get('author_id'))
        book.save()
        return redirect('book_list')
    return render(request, 'edit_book.html', {'book': book})

# View to delete a book (with permission check)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')
