# pages/urls.py
from django.urls import path

from react_sample.views import reactView

urlpatterns = [
    path('', reactView, name='home')
]