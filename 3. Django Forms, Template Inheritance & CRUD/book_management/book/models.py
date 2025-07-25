from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=80)
    authorName = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
