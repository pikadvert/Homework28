from django.shortcuts import render
from blog_hw31.models import Comment, Author, Article

def homework31(request):
    lastID = Comment.objects.last().id
    fivelastcomms = Comment.objects.filter(id__lte=lastID).order_by('-id')[:5]
    author = Author.objects.all().order_by('-name')[0]
    article = Article.objects.filter(author=author)[0]
    comments = Comment.objects.filter(article=article).order_by('-id')[:2]
    return render(request, 'articlesHW31.html', {'fivelastcomms': fivelastcomms, 'comments': comments})

