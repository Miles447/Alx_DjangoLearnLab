from .models import Author, Book
from rest_framework import serializers
from datetime import date
#custom serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
# Custom validation for publication year
    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the feature.")
        return value
#custom serializer for Author model
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
    
    books = BookSerializer(many=True, read_only=True)