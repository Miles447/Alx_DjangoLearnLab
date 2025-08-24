# posts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class UserSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

class PostSerializer(serializers.ModelSerializer):
    author = UserSlimSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "author", "title", "content", "created_at", "updated_at")

    def create(self, validated_data):
        # author from request.user
        request = self.context.get("request")
        validated_data["author"] = request.user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = UserSlimSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ("id", "post", "author", "content", "created_at", "updated_at")

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author"] = request.user
        return super().create(validated_data)
