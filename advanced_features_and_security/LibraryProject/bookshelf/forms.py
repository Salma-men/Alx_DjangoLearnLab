from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=255)  # Input field for the title
    author = forms.CharField(max_length=255)  # Input field for the author
