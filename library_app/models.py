from django.db import models

# Create your models here.

class Author1(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Reader(models.Model):
    name = models.CharField(max_length=120)

class Book1(models.Model):
    nameofbook = models.CharField(max_length=120)
    author = models.ManyToManyField(Author1, related_name='author')
    reader = models.ManyToManyField(Reader, related_name='reader')
    available = models.BooleanField(default=False, name='book available')

    class Meta:
        ordering = ['nameofbook']

    def __str__(self):
        return self.nameofbook




