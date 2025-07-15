from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Columns to show
    search_fields = ('title', 'author')  # Searchable fields

admin.site.register(Book, BookAdmin)