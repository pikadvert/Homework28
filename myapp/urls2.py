from django.urls import path
from .views import articles, archive

urlpatterns = [
    path('', articles, name='articles'),
    path('archive/', archive, name='archive')
]