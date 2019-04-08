from django.urls import path

from .views import ReactSampleListView, ReactSampleDetailView


urlpatterns = [
	path('', ReactSampleListView.as_view()),
	path('<pk>', ReactSampleDetailView.as_view()),
]