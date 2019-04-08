from rest_framework import serializers

from react_sample.models import ReactSample

class ReactSampleSerializer(serializers.ModelSerializer):
 	class Meta:
 		model = ReactSample
 		fields = ('title', 'content')
