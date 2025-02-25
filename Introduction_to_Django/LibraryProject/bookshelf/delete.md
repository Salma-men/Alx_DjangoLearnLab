# Delete a Book in Django Shell

```python
from bookshelf.models import Book

# Retrieve the book instance (assuming it exists)
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify deletion
print(Book.objects.all())  # Should print: <QuerySet []>
