# pages/urls.py
from django.urls import path

from board.views import boardView

urlpatterns = [
    path('', boardView, name='home')
]