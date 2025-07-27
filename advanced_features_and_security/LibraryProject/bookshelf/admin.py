from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'date_of_birth']
    search_fields = ['username', 'email']
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show
    search_fields = ('title', 'author')  # Searchable fields
    list_filter = ('publication_year',) 
admin.site.register(Book, BookAdmin)

admin.site.register(CustomUser, CustomUserAdmin)