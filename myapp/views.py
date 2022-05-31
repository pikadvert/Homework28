from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    return HttpResponse("Hey! Welcome to our site!")

def articles(request):
    return HttpResponse("This is a list with articles")

def users(request):
    return HttpResponse("This is a list of users")

def archive(request):
    return HttpResponse('This is archive')

def archive_of_artcls(request, article_number):
    return HttpResponse(f"This is archive of article number: #{article_number}.")

def user_number(request, user_number):
    return HttpResponse(f"This is the user number: #{user_number}.")

def article_text(request, article_number, slug_text=''):
    return HttpResponse(
        f"This is article with number: #{article_number} With text: {slug_text}" \
            if slug_text else (f"This is article with number: #{article_number}"))

def phoneregex(request, text2):
    return HttpResponse(f"It's your phone number: {text2}")

def newregex(request, text):
    return HttpResponse(f"it's regexp with text: {text}")