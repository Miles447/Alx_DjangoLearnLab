from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # other fields

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
