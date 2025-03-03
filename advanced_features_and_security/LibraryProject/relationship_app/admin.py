from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'date_of_birth')
    search_fields = ('username', 'email')
    ordering = ('username',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Function to create and assign permissions to groups
def setup_groups():
    content_type = ContentType.objects.get_for_model(Book)

    # Define groups
    editors_group, _ = Group.objects.get_or_create(name="Editors")
    viewers_group, _ = Group.objects.get_or_create(name="Viewers")
    admins_group, _ = Group.objects.get_or_create(name="Admins")

    # Get permissions
    can_view = Permission.objects.get(codename="can_view", content_type=content_type)
    can_create = Permission.objects.get(codename="can_create", content_type=content_type)
    can_edit = Permission.objects.get(codename="can_edit", content_type=content_type)
    can_delete = Permission.objects.get(codename="can_delete", content_type=content_type)

    # Assign permissions
    editors_group.permissions.add(can_create, can_edit)
    viewers_group.permissions.add(can_view)
    admins_group.permissions.add(can_create, can_edit, can_delete, can_view)

# Register Book model in admin
admin.site.register(Book)

# Ensure groups and permissions are set up when the server runs
setup_groups()