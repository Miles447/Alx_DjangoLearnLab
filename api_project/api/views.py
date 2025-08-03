from django.shortcuts import render
from rest_framework import generics 
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.authtoken.views import obtain_auth_token  
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class CustomObtainAuthToken(ObtainAuthToken):
    pass
