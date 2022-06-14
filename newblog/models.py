from django.db import models

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey

class User(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    a_like = GenericRelation('LikeDislike', related_query_name='article_new')


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey('newblog.Comment', null=True, blank=True, on_delete=models.DO_NOTHING,
                                related_name='comments')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment_like = GenericRelation('LikeDislike', related_query_name='comments')

    def __str__(self):
        return "{} by {}".format(self.text, self.user)


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
