from django.shortcuts import render
from .models import Book
from rest_framework import generics, permissions, filters
from .serializers import BookSerializer 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
#retrieve a single book

class BookListView(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] #allows anyone to view the list of books

    #add filter/search/order backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    #filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    #search fields (partial)
    search_fields = ['title', 'author']

    #ordering_fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] #default order
    
class BookDetailView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] #allows anyone to view the book details

#Create new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] #allows anyone to create a new book

#updte existing book
class BookUpdateView(generics.UpdateAPIView):    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] #allows anyone to update an existing book

#delete existing book    
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] #allows anyone to delete an existing book