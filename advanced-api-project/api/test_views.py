from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        """Set up test data and test client."""
        self.client = APIClient()

        # Create a test user and get token
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        # Create a test book
        self.book = Book.objects.create(title="Test Book", author="John Doe", published_date="2024-01-01")

        # Define URLs
        self.books_list_url = "/books_all/"
        self.book_detail_url = f"/books_all/{self.book.id}/"

    def test_get_books_list(self):
        """Test retrieving the list of books."""
        response = self.client.get(self.books_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", response.data[0]["title"])  # Use response.data instead of response.json()

    def test_create_book(self):
        """Test creating a new book."""
        data = {"title": "New Book", "author": "Jane Doe", "published_date": "2025-01-01"}
        response = self.client.post(self.books_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Test updating an existing book."""
        data = {"title": "Updated Book", "author": "John Doe", "published_date": "2024-01-01"}
        response = self.client.put(self.book_detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_unauthenticated_access(self):
        """Test accessing API without authentication."""
        self.client.force_authenticate(user=None)  # Remove authentication
        response = self.client.get(self.books_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
