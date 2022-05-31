from django.urls import path
from .views import archive_of_artcls, article_text

urlpatterns = [
    path('<int:article_number>/', article_text, name='article'),
    path('<int:article_number>/archive/', archive_of_artcls, name='archive_of_artcls'),
    path('<int:article_number>/<slug:slug_text>/', article_text),
]