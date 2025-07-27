from django.db import models

# Create your models here.
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_view", "Can view documents"),
            ("can_create", "Can create documents"),
            ("can_edit", "Can edit documents"),
            ("can_delete", "Can delete documents"),
        ]
