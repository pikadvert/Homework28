from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Book, Reader

admin.site.register(Reader)
admin.site.register(Book)
admin.site.register(Author)
