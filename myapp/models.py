from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=120)

class Author(models.Model):
    name = models.CharField(max_length=120)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='auth')

