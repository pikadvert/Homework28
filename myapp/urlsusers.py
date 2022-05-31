from django.urls import path
from .views import users, user_number

urlpatterns = [
    path('', users, name='users'),
    path('<int:user_number>/', user_number, name='user_number')
]