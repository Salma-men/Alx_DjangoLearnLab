from django import forms
from django.contrib.auth.models import User
from .models import UserProfile  
from .models import Post
from .models import Comment 


# Create a form to update the user profile (bio, profile picture)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # If you're using a custom UserProfile model
        fields = ['bio', 'profile_picture']  # Add the fields you want to include

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter comma-separated tags.")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        tags = self.cleaned_data['tags']
        instance.save()  # Save post first to get an ID

        if tags:
            instance.tags.set(*[tag.strip() for tag in tags.split(",")])

        return instance

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        tags = forms.CharField(required=False, help_text="Enter comma-separated tags.")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
