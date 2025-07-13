# CRUD Operations on the Book Model

This file documents the Create, Retrieve, Update, and Delete operations performed on the `Book` model in the Django shell.

---

## 🟢 CREATE

```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell>



#retrieve

book = Book.objects.get(title="1984")
book.title
# Output: '1984'

book.author
# Output: 'George Orwell'

book.publication_year
# Output: 1949




#update
book.title = "Nineteen Eighty-Four"
book.save()

book.title
# Output: 'Nineteen Eighty-Four'


#delete
book.delete()

Book.objects.all()
# Output: <QuerySet []>