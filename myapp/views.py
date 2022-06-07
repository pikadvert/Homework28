from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import random
import string
from random import randint

# Create your views here.

def main(request):
    return render(request, 'main.html')

def articles(request):
    return render(request, 'articles.html')

def users(request):
    return render(request, 'users.html')

def archive(request):
    return render(request, 'archive.html')

def archive_of_artcls(request, article_number):
    return HttpResponse(f"This is archive of article number: #{article_number}.")

def user_number(request, user_number):
    return HttpResponse(f"This is the user number: #{user_number}.")

# def article_text(request, article_number, slug_text=''):
#     return HttpResponse(
#         f"This is article with number: #{article_number} With text: {slug_text}" \
#             if slug_text else (f"This is article with number: #{article_number}"))

def article_text(request, article_number, slug_text=''):
    slug_text = slug_text
    article_number = article_number
    return render(request, 'slug.html' if slug_text else 'article_num.html', {'article_number': article_number,\
                                                                              'slug_text': slug_text})


# def random_slug(request):
#     letters = string.ascii_lowercase
#     rand_slug = ''.join(random.choice(letters) for i in range(10))
#     print(rand_slug)
#     return render(request, 'main.html', {'rand_slug': rand_slug})
#
# def random_num(request):
#     rand_num = random.randint(0, 100)
#     print(rand_num)
#     return render(request, 'main.html', {'rand_num': rand_num})


def phoneregex(request, text2):
    return HttpResponse(f"It's your phone number: {text2}")

def newregex(request, text):
    return HttpResponse(f"it's regexp with text: {text}")

