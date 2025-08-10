from django.shortcuts import render
from .models import Book
from rest_framework import generics, permissions
from .serializers import BookSerializer 

# Create your views here.
#retrieve a single book
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