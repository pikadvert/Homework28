from django.db import models

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey

class User(models.Model):
    name = models.CharField(max_length=100)

# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveSmallIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#
# class Dislike(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dislikes')
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveSmallIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')

class Article_new(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    a_like = GenericRelation('LikeDislike', related_query_name='article_new')
    # a_likes = GenericRelation(Like, related_query_name='article_new')
    # a_dislikes = GenericRelation(Dislike, related_query_name='article_new')

class Comment(models.Model):
    article = models.ForeignKey(Article_new, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    c_like = GenericRelation('LikeDislike', related_query_name='comment')
    # c_likes = GenericRelation(Like, related_query_name='comment')
    # c_dislikes = GenericRelation(Dislike, related_query_name='comment')

    class Meta:
        ordering = ['article']

    def __str__(self):
        return self.name

class Note(models.Model):
    note = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='note')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='noteusr')
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    n_like = GenericRelation('LikeDislike', related_query_name='note')
    # n_likes = GenericRelation(Like, related_query_name='note')
    # n_dislikes = GenericRelation(Dislike, related_query_name='note')

    class Meta:
        ordering = ['note']

    def __str__(self):
        return self.name

class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Dislake'),
        (LIKE, 'Like')
    )

    vote = models.SmallIntegerField(choices=VOTES, default=LIKE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.vote
