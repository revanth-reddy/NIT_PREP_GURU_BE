from .models import Slideshow, News, Companies, Exp
from rest_framework import serializers

class SlideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slideshow
        fields = ('image','slide_link','order')

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('news','link')

class CompSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Companies
        fields = ('name',)

class ExpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exp
        fields = ('name', 'job_title', 'year', 'placement', 'experience', 'problems')


class ExpDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exp
        fields = ('name', 'job_title', 'year', 'experience', 'problems')

