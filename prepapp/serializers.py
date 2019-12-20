from .models import Slideshow
from rest_framework import serializers

class SlideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slideshow
        fields = ('image','slide_link','order')