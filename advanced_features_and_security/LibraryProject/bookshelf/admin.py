from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Book  # Import the Book model

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Customize the display
    search_fields = ('title', 'author')  # Enable search functionality
    list_filter = ('publication_year',)  # Add filtering options

# Alternatively, you can use:
# admin.site.register(Book, BookAdmin)
# Extend Django's built-in UserAdmin to include the custom fields
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'profile_photo', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Register CustomUser with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)