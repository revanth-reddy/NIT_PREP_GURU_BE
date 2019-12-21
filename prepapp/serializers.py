from .models import Slideshow, News
from rest_framework import serializers

class SlideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slideshow
        fields = ('image','slide_link','order')

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('news','link')