from django.contrib import admin

from .models import Article_new, Comment, Note, User, LikeDislike
# Like, Dislike,

admin.site.register(Article_new)
admin.site.register(Comment)
admin.site.register(Note)
# admin.site.register(Like)
# admin.site.register(Dislike)
admin.site.register(User)
admin.site.register(LikeDislike)
