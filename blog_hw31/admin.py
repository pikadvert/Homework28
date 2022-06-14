from django.contrib import admin
from .models import Article, Comment, Author, Like, User


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Author)
admin.site.register(User)
