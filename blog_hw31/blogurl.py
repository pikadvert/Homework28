from django.urls import path
from .views import homework31

urlpatterns = [
    path('', homework31, name='hw31')
]
