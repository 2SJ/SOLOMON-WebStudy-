from rest_framework.generics import ListAPIView, RetrieveAPIView

from react_sample.models import ReactSample
from .serializer import ReactSampleSerializer

class ReactSampleListView(ListAPIView):
	queryset = ReactSample.objects.all()
	serializer_class = ReactSampleSerializer

class ReactSampleDetailView(RetrieveAPIView):
	queryset = ReactSample.objects.all()
	serializer_class = ReactSampleSerializer