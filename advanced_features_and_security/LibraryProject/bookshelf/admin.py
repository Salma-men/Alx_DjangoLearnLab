from django.contrib import admin
from .models import Book  # Import the Book model

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Customize the display
    search_fields = ('title', 'author')  # Enable search functionality
    list_filter = ('publication_year',)  # Add filtering options

# Alternatively, you can use:
# admin.site.register(Book, BookAdmin)
