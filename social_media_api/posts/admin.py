from django.contrib import admin

# Register your models here.
# posts/admin.py

from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at")
    search_fields = ("title", "content", "author__username")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "author", "created_at")
    search_fields = ("content", "author__username", "post__title")
