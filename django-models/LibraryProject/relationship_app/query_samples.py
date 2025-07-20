import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()


from relationship_app.models import Author, Book, Library, Librarian

# query 1 :All books by a specific author
author_name = 'John Doe'  # Replace with the author's name you want to query
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(f"- {book.title}")


#query 2 : List all books in a library
library_name = 'Central Library'
library = Library.objects.get(name=library_name)
print(f"\nBooks in {library_name}:")
for book in Library.books.all():
    print(f"- {book.title}")

#query 3 : retrieve the librarian from libraries
Library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarians for {library.name}: {librarian.name}")