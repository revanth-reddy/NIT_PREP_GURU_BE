from django.shortcuts import render
from .models import Slideshow, News
from .serializers import SlideSerializer, NewsSerializer
from rest_framework import viewsets

# Create your views here.
class SlideViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Slideshow.objects.all()
    serializer_class = SlideSerializer

class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
