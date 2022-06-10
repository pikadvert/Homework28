from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author1, Book1, Reader

admin.site.register(Reader)
admin.site.register(Book1)
admin.site.register(Author1)
