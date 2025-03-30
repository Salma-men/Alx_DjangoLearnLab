from django import forms
from django.contrib.auth.models import User
from .models import UserProfile  # Only if you created a custom UserProfile model

# Create a form to update the user profile (bio, profile picture)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # If you're using a custom UserProfile model
        fields = ['bio', 'profile_picture']  # Add the fields you want to include
