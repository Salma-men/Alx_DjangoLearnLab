# Summary of CRUD Operations

## 1️⃣ Create:
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```
_Output: `<Book: 1984 by George Orwell (1949)>`_

## 2️⃣ Retrieve:
```python
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
```
_Output: `1984 George Orwell 1949`_

## 3️⃣ Update:
```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
```
_Output: `Nineteen Eighty-Four`_

## 4️⃣ Delete:
```python
retrieved_book.delete()
print(Book.objects.all())
```
_Output: `<QuerySet []>`_
